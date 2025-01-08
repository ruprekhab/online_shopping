// Create an array of each category's numbers
let January = Object.values(salesData["2019-01"]);
let February = Object.values(salesData["2019-02"])
let March = Object.values(salesData["2019-03"]);
let April = Object.values(salesData["2019-04"]);
let May = Object.values(salesData["2019-05"]);
let June = Object.values(salesData["2019-06"]);
let July = Object.values(salesData["2019-07"]);
let August = Object.values(salesData["2019-08"]);
let September = Object.values(salesData["2019-09"]);
let October = Object.values(salesData["2019-10"]);
let November = Object.values(salesData["2019-11"]);
let December = Object.values(salesData["2019-12"]);

// Create an array of category labels
let labels = Object.keys(salesData["2019-01"]);


// Display the default plot
function init() {
    let trace = {
    x: labels,
    y: January,
    type: "bar",
    // name: "January Data"  
   
  };

  // Data Array
  let data = [trace];

  // Layout object
  let layout = {
    title: "Monthly Sales Data", // Set your chart title
    xaxis: { title: "Categories" }, // Label for x-axis
    yaxis: { title: "Sales Revenue" } // Label for y-axis
  };

  // Render the plot to the div tag with id "pie"
  Plotly.newPlot("plot", data, layout);
}

// On change to the DOM, call getData()
d3.selectAll("#selDataset").on("change", getData);

// Function called by DOM changes
function getData() {

  // Use D3 to select the dropdown menu
  let dropdownMenu = d3.select("#selDataset");

  // Assign the value of the dropdown menu option to a variable
  let dataset = dropdownMenu.property("value");

  // Initialize an empty array for the new country's data
  let newdata = [];

  // If/Else statement to assign the chosen country to the new dataset
  if (dataset == 'January') {
    newdata = January;
  }
  else if (dataset == 'February') {
    newdata = February;
  }
  else if (dataset == 'March') {
    newdata = March;
  }
  else if (dataset == 'April') {
    newdata = April;
  }
  else if (dataset == 'May') {
    newdata = May;
  }
  else if (dataset == 'June') {
    newdata = June;
  }
  else if (dataset == 'July') {
    newdata = July;
  }
  else if (dataset == 'August') {
    newdata = August;
  }
  else if (dataset == 'September') {
    newdata = September;
  }
  else if (dataset == 'October') {
    newdata = October;
  }
  else if (dataset == 'November') {
    newdata = November;
  }
  else if (dataset == 'December') {
    newdata = December;
  }

  // Call function to update the chart
  updatePlotly(newdata);
}

// Update the restyled plot's values
function updatePlotly(newdata) {
  Plotly.restyle("plot", { y: [newdata] });
}

init();
