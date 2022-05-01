let counter = 0;


var myImageElement = document.getElementById('myImage');
myImageElement.src = '/static/animal.jpg?rand=' + Math.random();

setInterval(function() {
      var myImageElement = document.getElementById('myImage');
      myImageElement.src = '/static/animal.jpg?rand=' + Math.random();
 }, 1000);


var myImageElement1 = document.getElementById('myImage1');
myImageElement1.src = '/static/animal2.jpg?rand=' + Math.random();

setInterval(function() {
      var myImageElement1 = document.getElementById('myImage1');
      myImageElement1.src = '/static/animal2.jpg?rand=' + Math.random();
 }, 1000);

function submit_form(){
   var form = document.getElementById("my_form");
   form.submit();
   return
 }

// store the divs of the four image windows
// let timeout =["first_slide"];

// // set a random time interval for the images for all the windows
// for (let s=0; s<timeout.length; s++){
//   imageSlide(timeout[s],"slides")
// }

// // function for the image carousel
// function imageSlide(im,cl){
//   let ele1=document.getElementById(im);
//   let x = ele1.getElementsByClassName(cl);

//   // only show one of the images in the image window, hide the rest
//   for (let k = 0; k < x.length; k++) {
//     x[k].style.display = "none";
//   }
//   counter++;
//   // if the counter reaches the end of the array of images, reset to the first image
//   if (counter > x.length) {
//       counter = 1
//     }
//   x[counter-1].style.display = "block";
//   // Change image at random intervals
//   timeout[im]=setTimeout(imageSlide, Math.floor((Math.random() * 5000) + 1000),im,"slides");
// }


// ---------------------------------------------------------------------------------------------------------------------------------------

// setInterval(function() {
    
//     var dt = new Date();
//     console.log(dt); //does not display anything on the console
    
//     const url = new URL(myImageElement.src);
//     url.search = 'time=' + dt.getTime();
//     img.src = url.href;
//     console.log(img.src + ' ' + dt); // does not display anything as well
//   }, 1000);








// function start_or_stop(bttn){
//   let im = bttn.name;
//   if(bttn.value==="Stop"){
//     Stop(timeout[im])
//     bttn.value="Start"
//   }
//   else if (bttn.value==="Start"){
//     bttn.value="Stop"
//     // restart the slider with a random time interval
//     timeout[im]=setTimeout(imageSlide, Math.floor((Math.random() * 5000) + 1000),im,"slides");
//   }
// }

// function Stop(x){
//   //console.log(x);
//   clearTimeout(x);
// }