const container = document.querySelector('.container');

function requestArticles(numArticles)
{
  fetch('127.0.0.1:5000/api/endpoint', {
    method:  'POST',
    headers: {
      'Content-Type' : 'application/json'
    }
  })
}

function loadArticles(numArticles = 9) {
  requestArticles()
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