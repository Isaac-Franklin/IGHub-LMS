/** @format */

// The data/time we want to countdown to
var stopTime = "Sept 30, 2022. 16:37:52";
var countDownDate = new Date(stopTime).getTime();

// Run myfunc every second
var myfunc = setInterval(function () {
	var now = new Date().getTime();
	var timeleft = countDownDate - now;

	// Calculating the days, hours, minutes and seconds left
	var days = Math.floor(timeleft / (1000 * 60 * 60 * 24));
	var hours = Math.floor((timeleft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
	var minutes = Math.floor((timeleft % (1000 * 60 * 60)) / (1000 * 60));
	var seconds = Math.floor((timeleft % (1000 * 60)) / 1000);

	// Result is output to the specific element
	var daysList = document.querySelectorAll("#days");
	Array.from(daysList).forEach((x) => {
		x.innerHTML = days + "d";
	});

	var hoursList = document.querySelectorAll("#hours");
	Array.from(hoursList).forEach((x) => {
		x.innerHTML = hours + "h ";
	});

	var minutesList = document.querySelectorAll("#mins");
	Array.from(minutesList).forEach((x) => {
		x.innerHTML = minutes + "m ";
	});

	var secondsList = document.querySelectorAll("#secs");
	Array.from(secondsList).forEach((x) => {
		x.innerHTML = seconds + "s ";
	});

	// Display the message when countdown is over
	if (timeleft < 0) {
		clearInterval(myfunc);
		document.getElementsByClassName("days").innerHTML = "";
		document.getElementsByClassName("hours").innerHTML = "";
		document.getElementsByClassName("mins").innerHTML = "";
		document.getElementsByClassName("secs").innerHTML = "";
		document.getElementsByClassName("end").innerHTML = "SUBMISSION CLOSED!";
	}
}, 1000);
