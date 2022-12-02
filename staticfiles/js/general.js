/** @format */

function displayDate() {
	let dateEnter = document.querySelector(".todayDate");
	// let date = new Date().toJSON().slice(0, 10);
	let date = new Date().toLocaleString({
		weekday: "short",
		month: "short",
		day: "2-digit",
		hour: "2-digit",
		minute: "2-digit",
	});
	dateEnter.innerHTML = `${date}`;
}
///// UNCOMMENT THE CODE BELOW TO START RUNNING TIME
// setInterval(displayDate, 1000);

///////
let navBarBtn = document.querySelector("#navbarbtn");
let sidebar2 = document.querySelector(".sidebar2");
let sidebar1 = document.querySelector(".sidebar");
let openMenu = document.querySelector("#navbarbtn");
let closeMenu = document.querySelector("#navbarbtn2");
let bodyImageSection = document.querySelector(".bodyImageSection");
let allSideBar = document.querySelector(".allSideBar");
var now = true;

navBarBtn.addEventListener("click", revealSideBar);
function revealSideBar() {
	sidebar2.style.display = "none";
	sidebar1.style.display = "block";
	openMenu.style.display = "none";
	closeMenu.style.display = "block";
	// bodyImageSection.style.width = "69.3rem";
}

function closeMenuBar() {
	sidebar2.style.display = "block";
	sidebar1.style.display = "none";
	openMenu.style.display = "block";
	closeMenu.style.display = "none";
	// bodyImageSection.style.width = " 82.2rem";
}

closeMenu.addEventListener("click", closeMenuBar);

let sideBarTexts = document.querySelectorAll(".sideBar1Text");

let revealSideBar2 = () => {
	sidebar2.style.display = "none";
	sidebar1.style.display = "block";
	openMenu.style.display = "none";
	closeMenu.style.display = "block";
};

// let killSideBar2 = () => {
// 	sidebar2.style.display = "block";
// 	sidebar1.style.display = "none";
// 	openMenu.style.display = "block";
// 	closeMenu.style.display = "none";
// };

sidebar2.addEventListener("mouseenter", revealSideBar2);

allSideBar.addEventListener("mouseleave", () => {
	sidebar2.style.display = "block";
	sidebar1.style.display = "none";
	openMenu.style.display = "block";
	closeMenu.style.display = "none";
});
