public class QuestionAnswers {
    private Answer firstParentAnswer;
    private Answer secondParentAnswer;
    private Boolean match;

    public boolean isMatch() {
        if (match == null) {
            match = Boolean.valueOf(
                (!firstParentAnswer.isAnswered() && !secondParentAnswer.isAnswered())
                || firstParentAnswer.equalsOtherAnswer(secondParentAnswer)
            );
        }
        return match.booleanValue();
    }
}
