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

var myImageElement3 = document.getElementById('myImage3');
myImageElement3.src = '/static/animal3.jpg?rand=' + Math.random();
var myImageElement4 = document.getElementById('myImage4');
myImageElement4.src = '/static/animal4.jpg?rand=' + Math.random();
var myImageElement5 = document.getElementById('myImage5');
myImageElement5.src = '/static/animal5.jpg?rand=' + Math.random();
var myImageElement6 = document.getElementById('myImage6');
myImageElement6.src = '/static/animal6.jpg?rand=' + Math.random();
var myImageElement7 = document.getElementById('myImage7');
myImageElement7.src = '/static/animal7.jpg?rand=' + Math.random();
var myImageElement8 = document.getElementById('myImage8');
myImageElement8.src = '/static/animal8.jpg?rand=' + Math.random();

setInterval(function() {
    myImageElement3 = document.getElementById('myImage3');
    myImageElement3.src = '/static/animal3.jpg?rand=' + Math.random();
    myImageElement4 = document.getElementById('myImage4');
    myImageElement4.src = '/static/animal4.jpg?rand=' + Math.random();
    myImageElement5 = document.getElementById('myImage5');
    myImageElement5.src = '/static/animal5.jpg?rand=' + Math.random();
    myImageElement6 = document.getElementById('myImage6');
    myImageElement6.src = '/static/animal6.jpg?rand=' + Math.random();
    myImageElement7 = document.getElementById('myImage7');
    myImageElement7.src = '/static/animal7.jpg?rand=' + Math.random();
    myImageElement8 = document.getElementById('myImage8');
    myImageElement8.src = '/static/animal8.jpg?rand=' + Math.random();
}, 10000);

function submit_form() {
    var form = document.getElementById("my_form");
    form.submit();
    return
}

// setInterval(function () {
//     fetch('https://example.com/profile/avatar', {
//         method: 'PUT',
//         body: formData
//     }).then(response => {
//         console.log(response.json())
//     })
// }, 5000)

// initialLoad = true;

// setInterval(function(){
//       if (initialLoad == true) {
//             new Chart(document.getElementById("myChart"), {
//                   type: 'bar',
//                   data: {
//                     labels: country,
//                     datasets: [
//                       {
//                         label: "Population (millions)",
//                         backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
//                         data: value
//                       }
//                     ]
//                   },
//                   options: {
//                     legend: { display: false },
//                     title: {
//                       display: true,
//                       text: 'Total Confirmed Cases of COVID in May'
//                     }
//                   }
//             });
//       } else {
            
//       }
// }, 1000);
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
//       counter = 3
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