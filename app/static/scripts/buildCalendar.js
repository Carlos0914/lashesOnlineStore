/**
 * Get the number of days of the month given as an offset from the current month
 * @param {number} offset
 * The integer value representing how many months to move forward or backward from the current date (positive for future dates, negative for previous dates)
 */
function daysInMonthFromNow(offset = 0) {
  let now = new Date();
  return new Date(now.getFullYear(), now.getMonth() + 1 + offset, 0).getDate();
}

/**
 * Get a number corresponding to the day of the week of the first day of the given month
 * @param {number} offset 
 * The integer value representing how many months to move forward or backward from the current date (positive for future dates, negative for previous dates)
 */
function getFirstDayOfMonth(offset = 0) {
  let now = new Date();
  return new Date(now.getFullYear(), now.getMonth() + offset, 1).getDay();
}

/**
 * Returns a matrix with 7 columns and the proper content to be displayed as a calendar on the frontend
 * @param {date} current_date
 * @param {number} monthsOffset
 */
function buildCalendar(monthsOffset = 0) {
  let prevNumberOfDays = daysInMonthFromNow(monthsOffset - 1);
  let currentNumberOfDays = daysInMonthFromNow(monthsOffset);

  let firstDay = getFirstDayOfMonth(monthsOffset);
  let mat = [];
  for (let i = prevNumberOfDays - firstDay + 1; i <= prevNumberOfDays; i++) {
    mat.push({ value: i, disabled: true });
  }
  mat = [
    ...mat,
    ...Array(currentNumberOfDays)
      .fill(0)
      .map((x, index) => ({ value: index + 1, disabled: false })),
  ];
  fill = 1;
  while (mat.length < 42) {
    // pad last row if necessary so it has exactly seven elements
    mat.push({ value: fill, disabled: true });
    fill += 1;
  }
  return Array.from({ length: mat.length / 7 }, (v, i) =>
    mat.slice(7 * i, 7 * (i + 1))
  );
}
