var x = 185;
var y = 420;
var dead = false;

var person;
var tombstone;

function preload() {  // load assets so they're ready
  person = loadImage("lego-character.png");
  tombstone = loadImage("coffin.png");
}

function setup() { 
  createCanvas(400, 500);
  randTime = second () + Math.floor(getRandomInt(4)+3);
  // line above making sure it'll always be at least 3 seconds + a random integer from 0-3
  color = 1;  // set color to 1 (red)
}

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

function draw() { 
  background(240);
  line(0,85,400,85);
  
  if(color == 0){
    fill (0, 255, 0);
  }
  else{
    fill (255, 0, 0);
  }
  
  if(second() == randTime) {
	randTime += getRandomInt(4)+3;
    
    if(color == 1 && dead == false) {
        color = 0;
      }
      else{
        color = 1;
      }
    }
  
    ellipse(width/9,height/12,40,40);
  
	if (second() == 59) {
		randTime = 0;
	}
  
  if (dead == true){              // if dead == true
    image(tombstone,x,y,78,60)    // show tombstone
  }
  else{                           // else
    image(person,x,y,50,80)       // show person
  }

}

// moves up, down, left, and right by 5
// if key pressed and person is not dead, move

function keyPressed() {
  if (keyCode === UP_ARROW && dead == false) {
    y = y - 5;
  } else if (keyCode === DOWN_ARROW && dead == false) {
   y = y + 5;
  }
  if (keyCode === LEFT_ARROW && dead == false) {
    x = x - 5;
  } else if (keyCode === RIGHT_ARROW && dead == false) {
    x = x + 5;
  }
  
  // if keystroke is inputted when the light color is red (=1) and the player position is below the line, set dead to true
  
  if (keyCode === UP_ARROW && color == 1 && y > 75) {
    dead = true;
  } else if (keyCode === DOWN_ARROW && color == 1 && y > 75) {
    dead = true;
  }
  if (keyCode === LEFT_ARROW && color == 1 && y > 75) {
    dead = true;
  } else if (keyCode === RIGHT_ARROW && color == 1 && y > 75) {
    dead = true;
  }
}