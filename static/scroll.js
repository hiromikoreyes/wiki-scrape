const container = document.querySelector('.container');
const body = document.querySelector('body')
var currentPath = window.location.href
var articlesRequested = false //Used to make sure the bottom scroll detection only sets off once per load

function overlayBuffering()
{
  buffer = document.createElement('img')
  buffer.src = 'https://cssauthor.com/wp-content/uploads/2018/06/Bouncy-Preloader.gif'
  buffer.classList.add("buffer")
  body.appendChild(buffer)
}

function removeBuffering()
{
  body.removeChild(buffer)
}


function requestArticles(content)
{
  fetch('/api-endpoint', {
    method:  'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({text: content})
  })  .then(response => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error('Request failed with status ' + response.status);
    }
  })
  .then(data => {
    loadArticles(9, data);
    removeBuffering();
    articlesRequested = false;
    console.log(data);
  })
  .catch(error => {
    body.innerHTML = '';
    const errorMessage = document.createElement('div');
    errorMessage.classList.add("heading");
    errorText = document.createTextNode("there was an error, refresh the page if that doesn't work there's probably something wrong with my code.");
    errorMessage.style = 'font-size: 48px;';
    errorMessage.appendChild(errorText);
    
    body.appendChild(errorMessage)
    console.log("broken!!")
  });
}


function loadArticles(numArticles, data) {
  for (let i = 0; i < numArticles; i++) {
    const article = document.createElement('div');
    article.classList.add("article")
    article.classList.add("fade-in-fast")
    container.appendChild(article)

    const title = document.createElement('div')
    title.classList.add("article-title")
    title_text = document.createTextNode(data[i]['title'])
    title.appendChild(title_text)
    article.appendChild(title)

    const bodyContent = document.createElement('div');
    bodyContent.classList.add("article-body")
    body_text = document.createTextNode(data[i]['content'] + '...')
    bodyContent.appendChild(body_text)
    article.appendChild(bodyContent)


  }
}



window.addEventListener('scroll', () => {
  // console.log(window.innerHeight)
  if(window.scrollY + window.innerHeight >= document.documentElement.scrollHeight && !articlesRequested){
    articlesRequested = true
    overlayBuffering()
    requestArticles(currentPath.slice(currentPath.indexOf('display') + 8,))
  }
})

//for once you land on the page
overlayBuffering()
requestArticles(currentPath.slice(currentPath.indexOf('display') + 8,))

