const container = document.querySelector('.container');
var articlesRequested = false

function overlayBuffering()
{
  buffer = document.createElement('div')
  buffer.classList.add("buffer")
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
    loadArticles(9, data)
    articlesRequested = false
    console.log(data);
  })
  .catch(error => {
    console.error(error);
  });
}


function loadArticles(numArticles, data) {
  for (let i = 0; i < numArticles; i++) {
    const article = document.createElement('div');
    article.classList.add("article")
    container.appendChild(article)

    const title = document.createElement('div')
    title.classList.add("article-title")
    title_text = document.createTextNode(data[i]['title'])
    title.appendChild(title_text)
    article.appendChild(title)

  }
}

requestArticles("Money")

window.addEventListener('scroll', () => {
  // console.log(window.innerHeight)
  if(window.scrollY + window.innerHeight >= document.documentElement.scrollHeight && !articlesRequested){
    articlesRequested = true
    requestArticles("Money")
  }
})