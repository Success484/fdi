// get current year
(function () {
    var year = new Date().getFullYear();
    document.querySelector("#currentYear").innerHTML = year;
})();




function getCurrentDate() {
    const currentDate = new Date();
    const year = currentDate.getFullYear();
    const month = String(currentDate.getMonth() + 1).padStart(2, '0'); // Adding 1 because months are zero-based
    const day = String(currentDate.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
}

// Get the element where you want to render the current date
const currentDateElement = document.getElementById('currentDate');

// Set the content of the element to the current date
currentDateElement.textContent = getCurrentDate();






function getCurrentTime() {
    const currentTime = new Date();
    const hours = String(currentTime.getHours()).padStart(2, '0');
    const minutes = String(currentTime.getMinutes()).padStart(2, '0');
    const seconds = String(currentTime.getSeconds()).padStart(2, '0');
    return `${hours}:${minutes}:${seconds}`;
}

// Get the element where you want to render the current time
const currentTimeElement = document.getElementById('currentTime');

// Set the content of the element to the current time
currentTimeElement.textContent = getCurrentTime();

// Update the time every second
// setInterval(function() {
//     currentTimeElement.textContent = getCurrentTime();
// }, 1000);

