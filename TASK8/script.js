function changeImage() {
  const color = document.getElementById("colorSelect").value;
  const image = document.getElementById("roseImage");
  image.src = `img/pictures/${color}.jpg`;
}

document.addEventListener("DOMContentLoaded", () => {
  const image = document.getElementById("roseImage");
  const list = document.getElementById("notificationList");

  // Hover -> suurennus
  image.addEventListener("mouseover", () => {
    image.classList.add("enlarged");
  });

  image.addEventListener("mouseout", () => {
    image.classList.remove("enlarged");
    list.innerHTML = "";
  });

  // Klikki -> ilmoituslistaan uusi rivi
  image.addEventListener("click", () => {
    const color = document.getElementById("colorSelect").value;
    const li = document.createElement("li");
    li.textContent = `You clicked the ${color} rose`;
    list.appendChild(li);
  });
});
