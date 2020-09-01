// this file is for getting familiar with JS

var colors = [
'white',
'black',
'custom'];

// update the third item in teh array
colors[2] = 'beige';

// get the element with and id of colors
var el= document.getElementById('colors');

// replace with third item from the array
el.textContent = colors[2];