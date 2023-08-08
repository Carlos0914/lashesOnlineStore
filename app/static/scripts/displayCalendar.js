let offset = 0;
let year = new Date().getFullYear();
let serverdata = JSON.parse(document.getElementById("agenda-data").textContent);
let container = document.getElementById("calendar");
const formCollapse = new bootstrap.Collapse("#appointmentDrawer", {
  toggle: false,
});

// Add column headers for year, month and day of the week
const months = [
  "Enero",
  "Febrero",
  "Marzo",
  "Abril",
  "Mayo",
  "Junio",
  "Julio",
  "Agosto",
  "Septiembre",
  "Octubre",
  "Noviembre",
  "Diciembre",
];
let div = document.createElement("div");
div.classList.add("d-flex");
for (element of ["Dom", "Lun", "Mar", "Mié", "Jue", "Vie", "Sáb"]) {
  let innerElement = document.createElement("div");
  innerElement.innerHTML = element;
  innerElement.style = `width: ${(100 / 7).toFixed(
    4
  )}%; border: 1px solid #BBB; display: flex; justify-content: center`;
  div.appendChild(innerElement);
}
container.appendChild(div);
function displayCalendar(offset = 0) {
  const prevButton = document.getElementById("buttonPrevMonth");
  prevButton.disabled = offset <= 0;
  const nextButton = document.getElementById("buttonNextMonth");
  nextButton.disabled = offset >= 5;
  document.querySelectorAll(".calendar-row").forEach((row) => row.remove());
  current_month = months[(new Date().getMonth() + offset) % 12];
  document.getElementsByClassName("calendar-month")[0].innerHTML =
    current_month;
  document.getElementsByClassName("calendar-year")[0].innerHTML =
    year + parseInt((new Date().getMonth() + offset) / 12);
  let data = buildCalendar(offset);

  // Add the squares for the days while checking availability for each
  container.addEventListener("click", (e) => {
    if (
      e.target.classList[0]?.includes("freespot") &&
      e.target.classList[0] !== "freespot-none"
    ) {
      clickHandler(
        year + parseInt((new Date().getMonth() + offset) / 12),
        current_month,
        e.target.innerText,
        serverdata[offset]?.[e.target.innerText - 1]
      );
      formCollapse.show();
    }
  });
  for (row of data) {
    div = document.createElement("div");
    div.classList.add("d-flex");
    div.classList.add("calendar-row");

    for (element of row) {
      let innerElement = document.createElement("div");
      innerElement.innerHTML = element.value;
      innerElement.style = `width: ${(100 / 7).toFixed(
        4
      )}%; aspect-ratio: 1; padding: 8px; border: 1px solid white;${
        element.disabled && "background: #AAA;"
      }`;
      let free_spots = serverdata[offset]?.[element.value - 1]?.spots;
      free_spots = !free_spots && free_spots !== 0 ? 8 : free_spots;
      if (!element.disabled) {
        innerElement.classList.add(
          free_spots > 4
            ? "freespot-high"
            : free_spots > 0
            ? "freespot-low"
            : "freespot-none"
        );
      }
      // copy the new innerElement into the parent div
      div.appendChild(innerElement);
    }
    container.appendChild(div);
  }
}

function clickHandler(year, month, day, day_data) {
  date_input = document.getElementById("id_appointment_date");
  document.getElementById(
    "selectedDate"
  ).innerText = `${day} de ${month} de ${year}`;
  date_input.value = `${year}-${months.indexOf(current_month) + 1}-${day}`;

  document.querySelectorAll(".badge").forEach((row) => row.remove());

  // cont = document.getElementById("hoursContainer");
  selectHour = document.getElementById("id_hour");
  selectHour.innerHTML = "";
  hours = [
    "09:00 AM",
    "10:00 AM",
    "11:00 AM",
    "12:00 PM",
    "01:00 PM",
    "02:00 PM",
    "03:00 PM",
    "04:00 PM",
    "05:00 PM",
    "06:00 PM",
  ];
  for (let i = 0; i < hours.length; ++i) {
    if (day_data.available[i] === null) {
      option = document.createElement("option");
      option.value = i;
      option.innerText = hours[i];
      selectHour.append(option);
    }
  }
}
displayCalendar(0);
