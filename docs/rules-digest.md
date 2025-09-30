# Rule Miner Digest

Generated from `tools/rule-miner/sample-output/rules.csv`.
Total matches: **6962** across **6** rule kinds.

## Distribution by kind

| Kind | Count | Share |
|------|-------|-------|
| unknown | 4983 | 71.6% |
| computed | 1378 | 19.8% |
| branching | 273 | 3.9% |
| validation | 220 | 3.2% |
| options | 98 | 1.4% |
| visibility | 10 | 0.1% |

## Top targets – unknown

| Target / Page | Hits |
|---------------|------|
| legacy\java\src\main\java\com\incap\engine\EasyEngine.java | 693 |
| legacy\java\src\main\java\com\incap\service\UserDataService.java | 466 |
| legacy\java\src\main\java\com\incap\service\MetadataService.java | 331 |
| legacy\java\src\main\java\com\incap\webapp\struts\tags\FieldTableTag.java | 259 |
| legacy\java\src\main\java\com\incap\model\report\comparison\ComparisonReportRunner.java | 210 |
| legacy\java\src\main\java\com\incap\engine\StorageEngine.java | 180 |
| legacy\java\src\main\java\com\incap\webapp\struts\action\DisplayChildIdKitAction.java | 157 |
| legacy\java\src\main\java\com\incap\webapp\struts\action\ProcessLoginAction.java | 94 |
| legacy\java\src\main\java\com\incap\webapp\struts\action\MonthlyCalendarDisplayAction.java | 87 |
| legacy\java\src\main\java\com\incap\model\report\comparison\ChildMedicationQuestionAnswersProvider.java | 80 |
| legacy\java\src\main\java\com\incap\model\visitation\WeeklyVisitation.java | 80 |
| legacy\java\src\main\java\com\incap\service\VisitationService.java | 76 |
| legacy\java\src\main\java\com\incap\model\report\comparison\ReportConfiguration.java | 75 |
| legacy\java\src\main\java\com\incap\engine\FormatVisitsForReport.java | 73 |
| legacy\java\src\main\java\com\incap\model\report\emergencycontact\ReportRunner.java | 71 |
| legacy\java\src\main\java\com\incap\webapp\viewbean\ReportDataViewBean.java | 68 |
| legacy\java\src\main\java\com\incap\webapp\struts\action\ParentingLongShortActionSub.java | 65 |
| legacy\java\src\main\java\com\incap\webapp\struts\action\ReportByAgreementAction.java | 63 |
| legacy\java\src\main\java\com\incap\webapp\struts\tags\MonthAndYearPickerTag.java | 54 |
| legacy\java\src\main\java\com\incap\webapp\struts\tags\TimePickerTag.java | 54 |

### Sample snippets (unknown)

- `legacy\java\src\main\java\com\incap\cache\ApplicationCache.java:29` — reset();
- `legacy\java\src\main\java\com\incap\cache\ApplicationCache.java:44` — reset();
- `legacy\java\src\main\java\com\incap\cache\ApplicationCache.java:53` — return readCache.get(key);
- `legacy\java\src\main\java\com\incap\cache\ApplicationCache.java:60` — masterCache = Collections.synchronizedMap(new HashMap());
- `legacy\java\src\main\java\com\incap\cache\ApplicationCache.java:61` — resyncReadCacheWithMasterCache();
- `legacy\java\src\main\java\com\incap\cache\ApplicationCache.java:75` — Object result = masterCache.put(key, value);
- `legacy\java\src\main\java\com\incap\cache\ApplicationCache.java:76` — resyncReadCacheWithMasterCache();
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:56` — unexpandedStringCache.reset();
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:63` — unexpandedStringCache.setActive(yesOrNo);
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:89` — return theBuildEngine(connection, sessionContext, viewBean,
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:134` — viewBean.setDoVariables(doVariables);
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:152` — System.out.println("********************** Here we go ****************************");
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:234` — theString = theString.replaceAll("&gt;", ">");
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:235` — theString = theString.replaceAll("&lt;", "<");
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:243` — int stringLength = sBuf.length() - 1;
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:245` — char currentChar = sBuf.charAt(currentPosition);
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:250` — && sBuf.charAt(currentPosition + 1) == '{') {
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:252` — int i2 = sBuf.indexOf("}}", currentPosition);
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:256` — while ((iNest = sBuf.indexOf("{{", iNest + 2)) > 0
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:258` — i2 = sBuf.indexOf("}}", i2 + 2);

## Top targets – computed

| Target / Page | Hits |
|---------------|------|
| legacy\java\src\main\java\com\incap\engine\EasyEngine.java | 185 |
| legacy\java\src\main\java\com\incap\service\UserDataService.java | 60 |
| legacy\java\src\main\java\com\incap\webapp\struts\tags\FieldTableTag.java | 49 |
| legacy\java\src\main\java\com\incap\engine\StorageEngine.java | 46 |
| addPageToSet(excludedPages | 30 |
| page | 29 |
| legacy\java\src\main\java\com\incap\webapp\struts\action\ProcessLoginAction.java | 25 |
| legacy\java\src\main\java\com\incap\model\init\Init.java | 24 |
| legacy\java\src\main\java\com\incap\utils\ImageUploadUtils.java | 20 |
| pageMetadata.getPageset() | 20 |
| legacy\java\src\main\java\com\incap\engine\ReadDB.java | 19 |
| pageContext.getOut() | 18 |
| pageContext | 18 |
| DisplayPageViewBean | 17 |
| legacy\java\src\main\java\com\incap\model\report\comparison\ComparisonReportRunner.java | 16 |
| legacy\java\src\test\java\com\incap\service\test\VisitationTest.java | 16 |
| pageMetadata.getTabset() | 14 |
| legacy\java\src\main\java\com\incap\webapp\struts\tags\PhotoTag.java | 14 |
| legacy\java\src\main\java\com\incap\webapp\visitation\WeeklyVisitationHTMLAdapter.java | 14 |
| legacy\java\src\test\java\com\incap\service\test\WeeklyVisitationTest.java | 14 |

### Sample snippets (computed)

- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:46` — private static final Logger logger = LogManager.getLogger(EasyEngine.class);
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:79` — DisplayPageViewBean viewBean = (DisplayPageViewBean) request
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:85` — String thisPageName = new StorageEngine(this).theStorageEngine(
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:109` — int indexOfUnderscore = thisPageName.indexOf('_');
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:117` — String pageSetName = thisPageName.substring(0, indexOfUnderscore);
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:118` — String pageName = thisPageName.substring(indexOfUnderscore + 1);
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:126` — Page page = MetadataService.getPage(pageSetName, lookupName);
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:128` — viewBean.setPageName(pageName);
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:129` — viewBean.setPageSetName(pageSetName);
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:132` — viewBean.setPageNameCurrent(page.getPageName());
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:132` — viewBean.setPageNameCurrent(page.getPageName());
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:169` — if (currentPage.equals(page)) {
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:185` — Boolean isAuthorized = currentPage.isPageAvailable (sessionContext);
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:187` — ( currentPage.getPageVisible().equals("yes")
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:187` — ( currentPage.getPageVisible().equals("yes")
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:188` — \|\| sessionContext.getToDoPages().contains(currentPage.getPageName()))) {
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:188` — \|\| sessionContext.getToDoPages().contains(currentPage.getPageName()))) {
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:188` — \|\| sessionContext.getToDoPages().contains(currentPage.getPageName()))) {
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:190` — result = currentPage.getPageName();
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:194` — if (currentPage.equals(lastPageSeen)) {

## Top targets – options

| Target / Page | Hits |
|---------------|------|
| legacy\java\src\main\java\com\incap\webapp\struts\action\OptionListAction.java | 16 |
| legacy\java\src\main\java\com\incap\engine\EasyEngine.java | 15 |
| legacy\java\src\main\java\com\incap\webapp\struts\tags\FieldTableTag.java | 14 |
| legacy\java\src\main\java\com\incap\service\UserDataService.java | 7 |
| legacy\java\src\main\java\com\incap\service\MetadataService.java | 6 |
| legacy\java\src\main\java\com\incap\service\VisitationService.java | 5 |
| legacy\java\src\main\java\com\incap\model\report\emergencycontact\ReportRunner.java | 4 |
| legacy\java\src\main\java\com\incap\webapp\struts\tags\DisplaySelectedChildrenNamesTag.java | 4 |
| legacy\java\src\main\java\com\incap\webapp\struts\tags\VisitationChildrenSelectionTag.java | 4 |
| legacy\java\src\main\java\com\incap\webapp\beans\DataTable.java | 3 |
| legacy\java\src\main\java\com\incap\engine\ReadDB.java | 2 |
| legacy\java\src\main\java\com\incap\webapp\struts\tags\ToDoListOutputter.java | 2 |
| legacy\java\src\main\java\com\incap\matching\Matcher.java | 1 |
| legacy\java\src\main\java\com\incap\webapp\beans\SelectList.java | 1 |
| legacy\java\src\main\java\com\incap\webapp\struts\AppInitializer.java | 1 |
| legacy\java\src\main\java\com\incap\webapp\struts\action\CallReportEngineActionSub.java | 1 |
| legacy\java\src\main\java\com\incap\webapp\struts\action\DisplayVisitationsAction.java | 1 |
| legacy\java\src\main\java\com\incap\webapp\struts\action\MonthlyCalendarDisplayAction.java | 1 |
| legacy\java\src\main\java\com\incap\webapp\struts\action\ParentingLongShortActionSub.java | 1 |
| legacy\java\src\main\java\com\incap\webapp\struts\action\PaymentRelayAction.java | 1 |

### Sample snippets (options)

- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:122` — if (lookupName.endsWith(".rtf")) {
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:123` — lookupName = lookupName.substring(0, lookupName.length() - 4);
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:123` — lookupName = lookupName.substring(0, lookupName.length() - 4);
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:2059` — Map optionsSelected = parseStoredMultiOptions(dataText);
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:2062` — Collection options = MetadataService.getOptionsForQuestion(question
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:2062` — Collection options = MetadataService.getOptionsForQuestion(question
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:2067` — for (Iterator optionIterator = options.iterator(); optionIterator
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:2067` — for (Iterator optionIterator = options.iterator(); optionIterator
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:2089` — if (optionsSelected.containsKey(oValueLower)) {
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:2113` — oExtraValue = (String) optionsSelected.get(oValueLower);
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:2441` — options = MetadataService.getInteractiveOptions("state_county",
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:2445` — options = MetadataService.getOptionsForQuestion(question.getId(),
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:2445` — options = MetadataService.getOptionsForQuestion(question.getId(),
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:2449` — for (Iterator optionIterator = options.iterator(); optionIterator
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:2449` — for (Iterator optionIterator = options.iterator(); optionIterator
- `legacy\java\src\main\java\com\incap\engine\ReadDB.java:107` — data = TagUtils.getInstance().filter(data);
- `legacy\java\src\main\java\com\incap\engine\ReadDB.java:107` — data = TagUtils.getInstance().filter(data);
- `legacy\java\src\main\java\com\incap\matching\Matcher.java:25` — ArrayList result = new ArrayList(firstCollection.size());
- `legacy\java\src\main\java\com\incap\model\report\emergencycontact\ReportRunner.java:89` — SelectList userChildren = UserDataService.getUserChildren(
- `legacy\java\src\main\java\com\incap\model\report\emergencycontact\ReportRunner.java:91` — for (Iterator iter = userChildren.getOptions().iterator(); iter

## Top targets – branching

| Target / Page | Hits |
|---------------|------|
| legacy\java\src\main\java\com\incap\service\MetadataService.java | 25 |
| legacy\java\src\main\java\com\incap\service\UserDataService.java | 19 |
| legacy\java\src\main\java\com\incap\webapp\struts\tags\FieldTableTag.java | 14 |
| legacy\java\src\main\java\com\incap\model\report\comparison\ComparisonReportRunner.java | 12 |
| legacy\java\src\main\java\com\incap\engine\PlanChildrenSupport.java | 10 |
| legacy\java\src\main\java\com\incap\engine\EasyEngine.java | 9 |
| out.print(viewBean.getPageNameNext()) | 8 |
| legacy\java\src\main\java\com\incap\engine\StorageEngine.java | 7 |
| legacy\java\src\main\java\com\incap\webapp\struts\action\ParentingLongShortActionSub.java | 7 |
| legacy\java\src\main\java\com\incap\webapp\struts\action\ReportByAgreementAction.java | 7 |
| legacy\java\src\main\java\com\incap\hibernate\SessionFactoryProvider.java | 6 |
| legacy\java\src\main\java\com\incap\webapp\struts\action\OptionListAction.java | 6 |
| pageMetadataList.iterator() | 6 |
| legacy\java\src\main\java\com\incap\model\report\comparison\CustomQuestionTitle.java | 5 |
| legacy\java\src\main\java\com\incap\model\report\comparison\ReportConfiguration.java | 5 |
| legacy\java\src\main\java\com\incap\model\visitation\WeeklyVisitation.java | 5 |
| legacy\java\src\main\java\com\incap\matching\Matcher.java | 4 |
| legacy\java\src\main\java\com\incap\model\visitation\state\VisitationStateSupport.java | 4 |
| (currentPage.getPreviousPageName().length() | 4 |
| (previousPage.getNextPageName().length() | 4 |

### Sample snippets (branching)

- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:130` — viewBean.setPageNamePrevious(findAdjacentPage(page, true,
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:130` — viewBean.setPageNamePrevious(findAdjacentPage(page, true,
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:133` — viewBean.setPageNameNext(findAdjacentPage(page, false, sessionContext));
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:133` — viewBean.setPageNameNext(findAdjacentPage(page, false, sessionContext));
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:155` — nextPageName = before ? lastPageSeen.getPreviousPageName()
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:156` — : lastPageSeen.getNextPageName();
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:158` — if (nextPageName == null \|\| nextPageName.equals(""))
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:161` — Page currentPage = MetadataService.getPage(nextPageName);
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:330` — char nextChar = sBuf.charAt(ii);
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:332` — if (Character.isLetterOrDigit(nextChar) \|\| nextChar == '_'
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:334` — word.append(nextChar);
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:940` — for (Iterator iter = doVariables.iterator(); iter.hasNext();) {
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:940` — for (Iterator iter = doVariables.iterator(); iter.hasNext();) {
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:941` — DoVariable doVariable = (DoVariable) iter.next();
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:1466` — if (result.next()) {
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:2069` — QuestionOption option = (QuestionOption) optionIterator.next();
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:2452` — QuestionOption option = (QuestionOption) optionIterator.next();
- `legacy\java\src\main\java\com\incap\engine\FormatVisitsForReport.java:36` — while (result.next()) {
- `legacy\java\src\main\java\com\incap\engine\FormatVisitsForReport.java:187` — while (result.next()) {
- `legacy\java\src\main\java\com\incap\engine\PlanChildrenSupport.java:41` — engine.getAnswerMap()).getOptions().iterator(); iter.hasNext();) {

## Top targets – validation

| Target / Page | Hits |
|---------------|------|
| legacy\java\src\main\java\com\incap\webapp\struts\action\ParentingLongShortActionSub.java | 18 |
| legacy\java\src\main\java\com\incap\webapp\struts\action\ReportByAgreementAction.java | 18 |
| legacy\java\src\main\java\com\incap\webapp\viewbean\ReportDataViewBean.java | 15 |
| legacy\java\src\main\java\com\incap\engine\EasyEngine.java | 9 |
| legacy\java\src\main\java\com\incap\webapp\struts\action\ProcessLoginAction.java | 9 |
| legacy\java\src\main\java\com\incap\webapp\struts\action\AccountAction.java | 7 |
| legacy\java\src\main\java\com\incap\webapp\struts\action\CallReportEngineActionSub.java | 7 |
| legacy\java\src\main\java\com\incap\webapp\struts\action\DisplayChildIdKitAction.java | 7 |
| legacy\java\src\main\java\com\incap\webapp\struts\action\ViewOtherAction.java | 7 |
| legacy\java\src\main\java\com\incap\webapp\struts\tags\DataTag.java | 7 |
| legacy\java\src\main\java\com\incap\webapp\struts\tags\FieldTag.java | 7 |
| legacy\java\src\main\java\com\incap\engine\StorageEngine.java | 6 |
| legacy\java\src\main\java\com\incap\webapp\struts\action\AuthenticatedSessionAction.java | 6 |
| legacy\java\src\main\java\com\incap\webapp\struts\action\PaymentRelayAction.java | 6 |
| legacy\java\src\main\java\com\incap\service\UserDataService.java | 5 |
| legacy\java\src\main\java\com\incap\model\report\comparison\CustomQuestionTitle.java | 4 |
| legacy\java\src\main\java\com\incap\service\MetadataService.java | 4 |
| legacy\java\src\main\java\com\incap\utils\ImageUploadUtils.java | 4 |
| legacy\java\src\main\java\com\incap\webapp\struts\tags\FieldTableTag.java | 4 |
| legacy\java\src\main\java\com\incap\webapp\struts\tags\HelpTableTag.java | 4 |

### Sample snippets (validation)

- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:165` — logger.error("findAdjacentPage: Page " + lastPageSeen.getPageName()
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:165` — logger.error("findAdjacentPage: Page " + lastPageSeen.getPageName()
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:264` — logger.error("Error - Unmached {{..}} -"
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:301` — logger.error("Error - Unmached [[..]] -"
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:465` — logger.error("processBracketMarker: Unrecognized Marker- "
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:503` — logger.error("Error - Unmached (..) in {{..}} -" + brackBlock);
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:542` — logger.error("Error - Unrecognized {{??? -" + brackBlock);
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:568` — logger.error("Error- If operator syntax- " + brackBlock);
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:760` — logger.error("Syntax error in Do Statement-" + text);
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:796` — logger.error("Syntax error in Do @ data- " + text);
- `legacy\java\src\main\java\com\incap\engine\EasyEngine.java:937` — logger.error("Undefined Do variable -" + text);
- `legacy\java\src\main\java\com\incap\engine\EngineConstants.java:238` — logger.error("More then " + styleName.length + " (Increase maxManyStyles");
- `legacy\java\src\main\java\com\incap\engine\StorageEngine.java:291` — logger.error("Failed to retrieve question for dbGroup=" + dbGroup
- `legacy\java\src\main\java\com\incap\engine\StorageEngine.java:338` — logger.error("Invalid page name for Select Topics - " + qName);
- `legacy\java\src\main\java\com\incap\engine\StorageEngine.java:401` — logger.error("Error processing- " + sName);
- `legacy\java\src\main\java\com\incap\engine\StorageEngine.java:446` — logger.error("DB Error 134B=" + ee);
- `legacy\java\src\main\java\com\incap\engine\StorageEngine.java:478` — logger.error("Error processing- " + sName);
- `legacy\java\src\main\java\com\incap\engine\StorageEngine.java:538` — logger.error("DB Error 134C=" + ee);
- `legacy\java\src\main\java\com\incap\engine\StorageEngine.java:570` — logger.error("DB Error 134B=" + ee);
- `legacy\java\src\main\java\com\incap\model\report\comparison\CustomQuestionTitle.java:78` — logger.error("Failed to load "

## Top targets – visibility

| Target / Page | Hits |
|---------------|------|
| pageMetadata.setTabsetVisible("yes".equals(ReadDB.readString( | 3 |
| (pageMetadata.isTabsetVisible()) | 3 |
| (!pageMetadata.isTabsetVisible() | 2 |
| legacy\java\src\main\java\com\incap\webapp\visitation\VisitationHTMLAdapterSupport.java | 2 |

### Sample snippets (visibility)

- `legacy\java\src\main\java\com\incap\service\MetadataService.java:835` — pageMetadata.setTabsetVisible("yes".equals(ReadDB.readString(
- `legacy\java\src\main\java\com\incap\service\MetadataService.java:835` — pageMetadata.setTabsetVisible("yes".equals(ReadDB.readString(
- `legacy\java\src\main\java\com\incap\service\MetadataService.java:835` — pageMetadata.setTabsetVisible("yes".equals(ReadDB.readString(
- `legacy\java\src\main\java\com\incap\webapp\struts\tags\PageMenuTag.java:140` — if (pageMetadata.isTabsetVisible()) {
- `legacy\java\src\main\java\com\incap\webapp\struts\tags\PageMenuTag.java:191` — if (pageMetadata.isTabsetVisible()) {
- `legacy\java\src\main\java\com\incap\webapp\struts\tags\PageMenuTag.java:238` — if (pageMetadata.isTabsetVisible()) {
- `legacy\java\src\main\java\com\incap\webapp\struts\tags\ToDoListOutputter.java:73` — if (!pageMetadata.isTabsetVisible()
- `legacy\java\src\main\java\com\incap\webapp\struts\tags\ToDoListOutputter.java:231` — if (!pageMetadata.isTabsetVisible()
- `legacy\java\src\main\java\com\incap\webapp\visitation\VisitationHTMLAdapterSupport.java:78` — visitation.setNoShow(getSafeParameter(request, PARAMETER_NO_SHOW)
- `legacy\java\src\main\java\com\incap\webapp\visitation\VisitationHTMLAdapterSupport.java:78` — visitation.setNoShow(getSafeParameter(request, PARAMETER_NO_SHOW)

---
_Regenerate with_: `python tools/rule-miner/summarize.py`
