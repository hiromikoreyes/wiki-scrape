const container = document.querySelector('.container');

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
    console.log(data);
  })
  .catch(error => {
    console.error(error);
  });
}


function loadArticles(numArticles = 9) {
  var list_articles = requestArticles("Money")
  console.log(list_articles)
  for (let i = 0; i < numArticles; i++) {
    const article = document.createElement('div');
    article.classList.add("article")
    container.appendChild(article)

    const title = document.createElement('div')
    title.classList.add("article-title")
    title_text = document.createTextNode("{{title}}")
    title.appendChild(title_text)
    article.appendChild(title)

  }
}

loadArticles()

window.addEventListener('scroll', () => {
  console.log(window.innerHeight)
  if(window.scrollY + window.innerHeight >= document.documentElement.scrollHeight){
    loadArticles()
  }
})