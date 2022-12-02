/** @format */

// MAIN JS JOB API FILES

/** @format */

{
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
}

///////
// MAIN JS JOB API ENDS HERE

console.log("working");
var details;
const loader = document.querySelector(".loader img");
const proxy = "https://cors-anywhere.herokuapp.com/";
await fetch(`${proxy}http://arbeitnow.com/api/job-board-api`)
	.then((response) => response.json())
	.then((data) => {
		details = data.data;
	});

function titleLenght(title, limit = 20) {
	let newTitle = [];
	if (title.lenght > limit) {
		title.split(" ").reduce((total, word) => {
			if (total + word.lenght <= limit) {
				newTitle.push(word);
			}
			return `${newTitle.join(" ")}...`;
		}, 0);
	} else {
		return title;
	}
}

function insertJobData(details) {
	for (let i = 0; i < details.length - 95; i++) {
		const element = details[i];
		let data = element;
		loader.style.display = "none";
		const jobDetails = `<div class="companyname"><h4>Company Name: ${data.company_name}</h4></div>
    <div class="jobtitle">Job Title: ${data.title}</div>
    <div class="jobdes"><h3></h3></div>
    <div class="jobLocation"><p>Location: ${data.location}</p></div>
    <div class="remote"><p>Remote: ${data.remote}</p></div>
	<button class="joburl"><a href="${data.url}" target="_blank">Click Here To Apply</a></button><br><br>`;

		document
			.querySelector(".jobsSection")
			.insertAdjacentHTML("beforeend", jobDetails);
	}
}

insertJobData(details);

//LOADER FUNCTION

// const loaderFxn = () => {
// 	const loader = document.querySelector("#")
// }
