const BASE_URL="http://127.0.0.1:8000"
$( document ).ready(()=> {
    $("#alertContainer").hide()
    fillQuizSelect()
});

$("#refreshButton").click((e) => {
    e.preventDefault();
    fillQuizSelect()
});

$("#quizSelect").change((e) => {
    e.preventDefault();
    getQuiz()
   
});

$("#solveButton").click((e) => {
    e.preventDefault();
    solveQuiz()
});

$("#resetButton").click((e) => {
    e.preventDefault();
    clearRadioButtons()
    
});

function getQuiz(){
    var id =  document.getElementById('quizSelect').value;
   
    $.ajax({
        type : "GET", 
        url: `${BASE_URL}/quizzes/${id}`,
        success: (quiz) => {
            quiz.questions.forEach(question => fillQuestionCard(question) );
        },
        error: (data) => {
        }
    });
}

function clearRadioButtons(){
    var ele = document.querySelectorAll('input[type=radio]:checked');
     for(var i=0;i<ele.length;i++){
        ele[i].checked = false;
     }
}

function fillQuizSelect(){
    const quizSelect = $('#quizSelect')

    $.ajax({
        type : "GET", 
        url: `${BASE_URL}/quizzes`,
        success: (quizzesData) => {
            quizSelect.find('option')
                            .not(':first')
                            .remove()
                            .end()
            quizzesData.forEach(quiz => quizSelect.append(`<option value="${quiz.id}">${quiz.label}</option>`) );
            $("#quizContainer").show()
            $("#alertContainer").hide()
        },
        error: (data) => {
            $("#quizContainer").hide()
            $("#alertContainer").show()
        }
    });
}

function fillQuestionCard(questionData){
    const container = $("#questionsContainer")
    var options =""
    questionData.options.forEach(option => options+=fillOption(option,questionData.id));
    container.append(` <div class="card mt-2 question-card" data-id="${questionData.id}">
    <h5 class="card-header">${questionData.label}</h5>
    <div class="card-body">
          ${options}
    </div>
  </div>`)
}

function fillOption(option,questionId){
    return ` <div class="form-check">
    <input class="form-check-input answer-option" type="radio" name="${questionId}" id="flexRadioDefault1" value="${option.id}">
    <label class="form-check-label" for="flexRadioDefault1">
      ${option.label}
    </label>
  </div>`

}

function solveQuiz(){
    const quizSelect= document.getElementById('quizSelect')
    var quizId =  quizSelect.value;
    const questionsAnswers= fillQuestionAnswerDic();
    if(quizId=="null"){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Please choose a quiz!',
          })
    }else{
        $.ajax({
            type : "POST", 
            url: `${BASE_URL}/quiz/${quizId}/solution`,
            data: JSON.stringify(questionsAnswers),
            contentType: "application/json",
            success: (solveData) => {
                Swal.fire(`Your score is ${solveData.correct_answers_count}/${solveData.total_questions_count}`)
            },
            error: (data) => {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Please try again!',
                  })
            }
        });
    }
  
}

function fillQuestionAnswerDic(){
    var questionCards = document.getElementsByClassName("question-card")
    var questionAnswerData={}
    for (var question of questionCards) {
        var id = $(question).attr('data-id')
        questionAnswerData[`${id}`]= $(question).find(`input[name='${id}']:checked`).val();
    }
    return questionAnswerData
}
