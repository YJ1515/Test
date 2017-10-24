"""Calculate Unit Score, Section Score, Question Score."""
import json


def calculate_score(unit_data):
    """Method to calculate score.

    :param unit_data : JSON, unit data with questions"""
    sum_of_section = 0.0

    # Get Section Score
    for questions in unit_data:
        question_data = questions.get("QUESTIONS")
        section = questions.get("SECTION_ID")

        sum_of_question = calculate_question_score(question_data, section)
        sum_of_section += sum_of_question

    print "\n\n--------------------------"
    print "Score of Section is {}".format(sum_of_section)

    print "\n\n--------------------------"
    print "Score of Unit is {}".format(sum_of_section/total_questions)


def calculate_question_score(question_data, section):
    """Method to calculate score.

    :param question_data : JSON, question data with choices
    :param section : int, section"""
    sum_of_question = 0.0

    # Get sum of each choice in question
    for index, questions in enumerate(question_data):
        choice_data = questions.get("CHOICES")
        selected_data = questions.get("SELECTED")

        selected_weight = None
        sum_of_choice = 0.0
        for choice in choice_data:
            value = choice.get("VAL")

            # Get weight for selected value
            if value == selected_data:
                selected_weight = choice.get("WEIGHT")
            sum_of_choice += value

        # Question Score
        question_score = selected_weight / sum_of_choice
        print "Score of Question {} in Section {} is {}".format(index + 1,
                                                                section,
                                                                question_score)
        sum_of_question += question_score
    return sum_of_question

if(__name__ == "__main__"):

    # Read JSON data fromm file.
    with open('test_data.json') as data_file:
        unit_data = json.load(data_file).get("UNIT")
        total_questions = len(unit_data)

    calculate_score(unit_data)


"""
Output

Score of Question 1 in Section 1 is 0.166666666667
Score of Question 2 in Section 1 is 0.0153846153846
Score of Question 3 in Section 1 is 0.00458015267176
Score of Question 1 in Section 2 is 0.166666666667
Score of Question 2 in Section 2 is 0.0153846153846
Score of Question 3 in Section 2 is 0.00458015267176
Score of Question 1 in Section 2 is 0.166666666667
Score of Question 2 in Section 2 is 0.0153846153846
Score of Question 3 in Section 2 is 0.00458015267176


--------------------------
Score of Section is 0.559894304169


--------------------------
Score of Unit is 0.186631434723
"""
