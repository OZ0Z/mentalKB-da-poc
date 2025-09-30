import importlib.util
import sys
from pathlib import Path

base = Path(__file__).resolve().parents[1]
package_name = 'docassemble.mentalkb'
package_path = base / 'docassemble' / 'mentalkb'
package_module = importlib.util.module_from_spec(importlib.util.spec_from_loader(package_name, loader=None))
package_module.__path__ = [str(package_path)]
sys.modules[package_name] = package_module

loader_spec = importlib.util.spec_from_file_location(f'{package_name}.loader', package_path / 'loader.py', submodule_search_locations=[str(package_path)])
loader = importlib.util.module_from_spec(loader_spec)
sys.modules[f'{package_name}.loader'] = loader
loader_spec.loader.exec_module(loader)

rules_spec = importlib.util.spec_from_file_location(f'{package_name}.rules', package_path / 'rules.py', submodule_search_locations=[str(package_path)])
rules = importlib.util.module_from_spec(rules_spec)
sys.modules[f'{package_name}.rules'] = rules
rules_spec.loader.exec_module(rules)

Page = loader.Page
Question = loader.Question
build_fields = rules.build_fields
resolve_next_page = rules.resolve_next_page


class DummyKB:
    def __init__(self):
        self.pages = {
            'A': Page(id='1', name='A', title='A', header=None, pageset='set', order=0,
                      next_name='B', previous_name=None, visible=True, availability=None, page_type=None),
            'B': Page(id='2', name='B', title='B', header=None, pageset='set', order=1,
                      next_name=None, previous_name='A', visible=True, availability=None, page_type=None),
            'C': Page(id='3', name='C', title='C', header=None, pageset='set', order=2,
                      next_name=None, previous_name='B', visible=False, availability=None, page_type=None),
        }

    def get_page_sequence(self, pageset_name):
        return [self.pages['A'], self.pages['B'], self.pages['C']]

    def options_for(self, question_id):
        return []

    def has_options(self, question_id):
        return False

    def da_datatype_for(self, kind: str) -> str:
        return 'text'


def test_resolve_next_page_prefers_explicit_next():
    kb = DummyKB()
    result = resolve_next_page(kb, 'set', kb.pages['A'], visited=['A'])
    assert result is kb.pages['B']


def test_resolve_next_page_skips_hidden():
    kb = DummyKB()
    kb.pages['A'].next_name = None
    result = resolve_next_page(kb, 'set', kb.pages['A'], visited=['A'])
    assert result is kb.pages['B']


def test_build_fields_adds_visibility():
    kb = DummyKB()
    question = Question(id='101', page_id='1', group='Parent', field='contact_phone',
                         kind='text', prompt='Parent contact phone', required=True, sort=0)
    fields = build_fields(kb, [question], {'has_parental_rights': False})
    assert fields[0]['show if'] == 'has_parental_rights'
