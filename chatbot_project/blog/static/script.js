const inputMessage = document.getElementById('textInput')
const submit =document.getElementById('buttonInput')
const chatbotBox = document.getElementById('chatbot')

submit.addEventListener('click',handleSubmit)


async function handleSubmit(){

    const message = inputMessage.value
    const htmlMessageInsert="<p class='userText'>User: <span>"+message+"</span></p>"
    chatbotBox.innerHTML += htmlMessageInsert
    console.log(inputMessage.value)
    inputMessage.value = '';

    

}