function changeImage() {
  const selected = document.getElementById("colorSelect").value;
  document.getElementById("roseImage").src = `img/${selected}.jpg`;
}
