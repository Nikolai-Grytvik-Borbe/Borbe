const url = "http://127.0.0.1:8000/blog/";
const postDiv = document.getElementById("posts");

function validateResponse(response) {
    if (!response.ok) {
        if (response.status == 404) {
            console.log("Not found")
        }
        throw Error(response.statusText);
    }
    return response.json();
}

function showPost(post) {
    const card = document.createElement("div");

    const header = document.createElement("h3");
    header.textContent = post.title;

    const info = document.createElement("p");
    info.textContent = `${post.author.name} - ${post.updated_time}`

    const text = document.createElement("div");
    text.textContent = post.content;
    card.append(header, info, text)
    postDiv.appendChild(card)
}

fetch(url)
    .then(validateResponse)
    .then(
        data => data.forEach(
            element => showPost(element)
        )
    );