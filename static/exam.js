document.getElementById('button').addEventListener('click', (event) => {

    event.preventDefault()

    answers = document.getElementsByName('answer')
    actual_answers = document.getElementsByName('actual_answer')
    remainders = document.getElementsByName('remainder')
    actual_remainders = document.getElementsByName('actual_remainder')

    console.log(answers)
    console.log(actual_answers)
    console.log(remainders)
    console.log(actual_remainders)

    for (let i = 0; i < 9; i++) {
        if (Number(answers[i].value) === Number(actual_answers[i].value)) {
            $(`#content${i}`).before('<p style="font-size: larger; color: green;">Well done!</p>');
        }
        else {
            $(`#content${i}`).before(`<p style="font-size: larger; color: rgb(136, 0, 0);">Wrong answer! Answer should be ${actual_answers[i].value}</p>`);
        }
        $(`#content${i}`).css('height: 500px;');
    }

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
        $(`#content${i}`).css('height: 500px;');
    }
});
