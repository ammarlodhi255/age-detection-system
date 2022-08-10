let imageChooser = document.getElementById("imageChooser");
let img = document.getElementById("image");
img.hidden = true;

imageChooser.onchange = () => {
    console.log('yes');
  const reader = new FileReader();
  reader.onload = () => {
    let image = reader.result;
    img.setAttribute("src", image);
    imageChooser.parentElement.hidden = true;
    img.hidden = false;
  };
  reader.readAsDataURL(imageChooser.files[0]);
};
