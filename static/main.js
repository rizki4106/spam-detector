const btn = document.querySelectorAll(".btn-score")

function scoreToggle(type, value, index){
    if(index === 1){
        btn[1].addEventListener("click", () => {
            let val = ''
            if(type === 'ham'){
                val = 'spam'
            }else{
                val = 'ham'
            }
            showHide()
            sentData(type,val)
        })
    }else{
        btn[0].addEventListener('click', () => {
            sentData(type, value)
            showHide()
        })
    }
}

function showHide(){
    const score = document.querySelector('.col-score')
    score.classList.add("hide-score")
}

function sentData(message, type){
    // dataset
    const data = new FormData()
    data.append('type', type)
    data.append('message', message)

    // sent the data

    const xhr = new XMLHttpRequest()
    xhr.onreadystatechange = () => {
        if(xhr.status === 200 && xhr.readyState === 4){
            const response = xhr.responseText
            console.log(response)
        }
    }
    xhr.open("POST", "/score", true)
    xhr.send(data)
}

function shareButton(index){
    switch(index){
        case 0:
            window.open(`http://www.facebook.com/sharer.php?u=${window.location.href}`)
            break;
        case 1:
            window.open(`https://twitter.com/share?url=${window.location.href}`)
            break;
        default:
            console.log("there's something wrong")
    }
}