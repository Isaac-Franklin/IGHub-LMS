/** @format */

let navbtn = document.querySelector(".navcontrol");
let sidebar = document.querySelector(".instruct-bottom");
let navbtn2 = document.querySelector(".navcontro2");

let reveal = () => {
	// setTimeout(() => {
	// 	sidebar.style.display = "block";
	// }, 200);
	sidebar.style.display = "block";
	sidebar.classList.add("slidein");
	navbtn.style.display = "none";
	navbtn2.style.display = "block";
};

let hidesidebar = () => {
	navbtn.style.display = "block";
	sidebar.classList.add("slideback");
	navbtn2.style.display = "none";
	setTimeout(() => {
		sidebar.style.display = "none";
		location.reload();
	}, 800);
};

navbtn.addEventListener("click", reveal);
navbtn2.addEventListener("click", hidesidebar);
