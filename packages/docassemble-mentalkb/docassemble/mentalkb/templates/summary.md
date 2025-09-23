# MentalkB Interview Summary

Generated: ${ format_datetime(now()) }

% for key, value in sorted(user_dict().items()):
% if key.startswith('q_'):
- **${ key[2:] }**: ${ value }
% endif
% endfor
