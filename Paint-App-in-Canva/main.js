let ctx;
let savedImageData;
let dragging=false;
let strokeColor="black";
let fillColor="black";
let canvas;
let line_width=2;
let polygonSides=6;
let currentTool='brush';//Error can be here
let canvasWidth=600;
let canvasHeight=600;
let isDragging;
let offsetX;
let offsetY;
let circleCount=0;
let rectangleCoordinates = []
let currentRectangleCoordinates = {
startX: 0, 
startY: 0,
endX : 0,
endY : 0,
}

// startX, startY, endX, endY




function onMouseUp(event)
{
    document.body.removeEventListener("mousemove",onMouseMove);
    document.body.removeEventListener("mouseup",onMouseUp);
    // console.log(rectangleCoordinates);
    circleCount++;
}

function clearCanvas(){
    var c = document.getElementById("my-canvas");
    var ctx = c.getContext("2d");
   
    ctx.clearRect(0, 0, 600, 300);
    rectangleCoordinates = [];
    circleCount=0;
}

function deleteDBL(rectX,rectY,width,height){
    ctx.clearRect(rectX,rectY,width,height);
}


class ShapeBoundingBox{
    constructor(left,top,width,height){
        this.left=left;
        this.top=top;
        this.width=width;
        this.height=height;
    }
}

class MouseDownPos{
    constructor(x,y){
        this.x=x;
        this.y=y;
    }
}

class Location{
    constructor(x,y){
        this.x=x;
        this.y=y;
    }
}

class PolygonPoint{
    constructor(x,y){
        this.x=x;
        this.y=y;
    }
}

let shapeBoundingBox=new ShapeBoundingBox(0,0,0,0);
let mousedown = new MouseDownPos(0,0);
let loc= new Location(0,0);

document.addEventListener('DOMContentLoaded',setupCanvas);

function setupCanvas(){
    canvas=document.getElementById('my-canvas');
    ctx=canvas.getContext('2d');
    ctx.strokeStyle=strokeColor;
    ctx.lineWidth=line_width; 
    canvas.addEventListener("mousedown", ReactToMouseDown);
    canvas.addEventListener("mousemove", ReactToMouseMove);
    canvas.addEventListener("mouseup", ReactToMouseUp);
    
canvas.addEventListener('dblclick', function(e){ 
    loc = GetMousePosition(e.clientX,e.clientY)
    rectangleCoordinates.forEach((elem)=>{
        if(loc.x >= elem.startX && loc.x <= elem.endX && loc.y >= elem.startY && loc.y <= elem.endY){
          ctx.clearRect(elem.startX,elem.startY,Math.abs(elem.startX-elem.endX),Math.abs(elem.startY - elem.endY))
        }

    })

});
}


function ChangeTool(toolClicked)
{

    document.getElementById('open').className="";

    document.getElementById('rectangle').className="";

    document.getElementById(toolClicked).className='selected';
    currentTool=toolClicked;
}


function GetMousePosition(x,y){
    let canvasSizeData=canvas.getBoundingClientRect();
    return {x:(x-canvasSizeData.left)*(canvas.width/canvasSizeData.width),
    y:(y-canvasSizeData.top)*(canvas.height/canvasSizeData.height)
    };
}

//saving canvas image
function SaveCanvasImage(){
    savedImageData=ctx.getImageData(0,0,canvas.width,canvas.height);
}

//redrawing Canvas Image
function RedrawCanvasImage(){
    ctx.putImageData(savedImageData,0,0)
}

//update mouse position
function UpdateRubberbandSizeData(loc)
{
    shapeBoundingBox.width=Math.abs(loc.x-mousedown.x);
    shapeBoundingBox.height=Math.abs(loc.y-mousedown.y);

    if(loc.x > mousedown.x){
        shapeBoundingBox.left=mousedown.x;
    }else{
        shapeBoundingBox.left=loc.x;
    }

    if(loc.y > mousedown.y){
        shapeBoundingBox.top = mousedown.y;
    }else{
        shapeBoundingBox.top=loc.y;
    }

}

//getting angle using x and y
function getAngleUsingXAndY(mouselocX,mouselocY){
    let adjacent = mousedown.x-mouselocX;
    let opposite=mousedown.y-mouselocY;
    return radiansToDegrees(Math.atan2(opposite,adjacent));
}

//radians to degree
function radiansToDegrees(rad){
    return (rad*(180/Math.PI)).toFixed(2);
}

//degrees to radians
function degreesToRadians(degrees){
    return degrees*(Math.PI/180);
}

//update rubberband on move
function UpdateRubberbandOnMove(loc){
    UpdateRubberbandSizeData(loc);
    drawRubberbandShape(loc);

}

//drawing rubberband shape
function drawRubberbandShape(loc){
    ctx.strokeStyle=strokeColor;
    // ctx.fillStyle=fillColor;
        // ctx.strokeRect(shapeBoundingBox.left,shapeBoundingBox.top,
        // shapeBoundingBox.width,shapeBoundingBox.height);

    var x=shapeBoundingBox.left;
    var y=shapeBoundingBox.top;
    var width=shapeBoundingBox.width;
    var height=shapeBoundingBox.height;

    ctx.fillStyle = getRndColor();  
    ctx.fillRect(x, y, width, height);

}

function getRndColor() {
    var r = 255*Math.random()|0,
        g = 255*Math.random()|0,
        b = 255*Math.random()|0;
    return 'rgb(' + r + ',' + g + ',' + b + ')';
}

//react to mouse down
function ReactToMouseDown(e){
    canvas.style.cursor="crosshair";
    loc=GetMousePosition(e.clientX,e.clientY);
    currentRectangleCoordinates.startX = loc.x
    currentRectangleCoordinates.startY = loc.y
    SaveCanvasImage();
    mousedown.x=loc.x;
    mousedown.y=loc.y;
    dragging=true;

    //todo handle brush
}

//REact to mouse move
function ReactToMouseMove(e){
    canvas.style.cursor="crosshair";
    loc= GetMousePosition(e.clientX,e.clientY);
    if(dragging)
    {
        RedrawCanvasImage();
        UpdateRubberbandOnMove(loc);
    }
 
   
    //TODO handle brush
}

//react to mouse up
function ReactToMouseUp(e){
    canvas.style.cursor="default";
    loc=GetMousePosition(e.clientX,e.clientY);
    currentRectangleCoordinates.endX = loc.x;
    currentRectangleCoordinates.endY = loc.y;
    let temp = JSON.parse(JSON.stringify(currentRectangleCoordinates));
    rectangleCoordinates.push(temp)
    RedrawCanvasImage();
    UpdateRubberbandOnMove(loc);
    dragging =false;
    usingBrush=false;
    // ctx.fillStyle = "blue";
    // ctx.fill();

}

//save image
function SaveImage(){
    var imageFile=document.getElementById('img-file');
    imageFile.setAttribute('download','image.png');
    imageFile.setAttribute('href',canvas.toDataURL());
}

//openImage
function OpenImage(){
    let img = new Image();
    img.onload=function(){
        ctx.clearRect(0,0,canvas.width,canvas.height);
        ctx.drawImage(img,0,0);
    }
    img.src='image.png';
}
//********************************************************************* */

function mouseDown(event) 
{
		var i;
		var highestIndex = -1;		
		var bRect = canvas.getBoundingClientRect();
	
		mouseX = (event.clientX - bRect.left)*(canvas.width/bRect.width);
		mouseY = (event.clientY - bRect.top)*(canvas.height/bRect.height);
		
		//To find that which circle has been clicked
		for (i=0; i < circleCount; i++) {
			if	(isCircleClicked(circles[i], mouseX, mouseY)) {
				draggingMove = true;
				if (i > highestIndex) {
					dragX = mouseX - rectangleCoordinates[i].startX;
					dragY = mouseY - rectangleCoordinates[i].startY;
					highestIndex = i;
					dragIndexMove = i;
				}				
			}
		}
		if (draggingMove) {
			window.addEventListener("mousemove", mouseMove, false);
			//Remove the circle and then push it to the top of the array
			rectangleCoordinates.push(rectangleCoordinates.splice(dragIndexMove,1)[0]);
			
		}
		canvas.removeEventListener("mousedown", mouseDown, false);
		window.addEventListener("mouseup", mouseUp, false);
		
		if (event.preventDefault) {
				event.preventDefault();
			} 
		else if (event.returnValue) {
				event.returnValue = false;
			} 
		return false;
}
	
	function mouseUp(event) {

		canvas.addEventListener("mousedown", mouseDown, false);
		window.removeEventListener("mouseup", mouseUp, false);
		if (draggingMove) {
			draggingMove = false;
			window.removeEventListener("mousemove", mouseMove, false);
		}
	}

	function mouseMove(event) {
		
		var posX;
		var posY;
		var shapeRad = circles[circleCount-1].rad;
		var minX = shapeRad;
		var maxX = canvas.width - shapeRad;
		var minY = shapeRad;
		var maxY = canvas.height - shapeRad;
		
		var bRect = canvas.getBoundingClientRect();
		mouseX = (event.clientX - bRect.left)*(canvas.width/bRect.width);
		mouseY = (event.clientY - bRect.top)*(canvas.height/bRect.height);
		
		posX = mouseX - startX;
		posX = (posX < minX) ? minX : ((posX > maxX) ? maxX : posX);
		posY = mouseY - dragY;
		posY = (posY < minY) ? minY : ((posY > maxY) ? maxY : posY);
		
		circles[circleCount-1].x = posX;
		circles[circleCount-1].y = posY;
		
		drawCircles();
	}