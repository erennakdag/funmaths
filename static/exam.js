// dynamically changes the exam page so the user knows what they did well and what not

document.getElementById('button').addEventListener('click', (event) => {

    event.preventDefault();

    // getting user answers and the actual answers
    answers = document.getElementsByName('answer');
    actual_answers = document.getElementsByName('actual_answer');
    remainders = document.getElementsByName('remainder');
    actual_remainders = document.getElementsByName('actual_remainder');

    // for debug
    console.log(answers);
    console.log(actual_answers);
    console.log(remainders);
    console.log(actual_remainders);

    // looping through the first 3 operations
    for (let i = 0; i < 9; i++) {
        if (Number(answers[i].value) === Number(actual_answers[i].value)) {
            $(`#content${i}`).before('<p style="font-size: larger; color: green;">Well done!</p>');
        }
        else {
            $(`#content${i}`).before(`<p style="font-size: larger; color: rgb(136, 0, 0);">Wrong answer! Answer should be ${actual_answers[i].value}</p>`);
        }
    }

    // looping through the last operation (division)
    for (let i = 9; i < 12; i++) {
        if (Number(answers[i].value) === Number(actual_answers[i].value)) {

            if (Number(remainders[i - 9].value) !== Number(actual_remainders[i - 9].value)) {
                $(`#content${i}`).before(`<p style="font-size: larger; color: rgb(136, 0, 0);">Wrong answer! Remainder should be ${actual_remainders[i - 9].value}</p>`);
            }
            else {
                $(`#content${i}`).before('<p style="font-size: larger; color: green;">Well done!</p>');
            }

        }
        else {
            $(`#content${i}`).before(`<p style="font-size: larger; color: rgb(136, 0, 0);">Wrong answer! Answer should be ${actual_answers[i].value}</p>`);
        }
    }
});
