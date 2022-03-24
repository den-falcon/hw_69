let requestButtons = document.getElementsByName('request-button')
let answerField = document.getElementById('answer-field')
let answer = document.getElementById('answer')

async function request(event, method='POST') {
    let eventTarget = event.target;
    let url = eventTarget.dataset.href;
    // let elementId = eventTarget.dataset.elementId;
    let csrf = document.cookie.match(/csrftoken=([\w-]+)/)[1];
    let data = {
        'A': document.getElementById('input-a').value,
        'B': document.getElementById('input-b').value
    }
    let response = await fetch(url, {
        'method': 'POST',
        'body': JSON.stringify(data),
        'headers': {
            'X-CSRFToken': csrf
        }
    });
    let responseBody = await response.json();
    console.log(responseBody)
    if (response.ok) {
        answerField.style.backgroundColor = '#2cb674';
        answer.innerText = responseBody['answer'];
    } else {
        answerField.style.backgroundColor = '#b42e2e';
        answer.innerText = responseBody['error'];
    }
}


window.addEventListener('load', function() {
    for (let i=0; i<requestButtons.length; i++) {
            requestButtons[i].addEventListener('click', request)
    }
})