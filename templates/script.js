function checkSelectedValues() {
  var selectElement = document.getElementById("destinationSelect");
  var selectedOptions = [];

  for (var i = 0; i < selectElement.options.length; i++) {
    if (selectElement.options[i].selected) {
      selectedOptions.push(selectElement.options[i].value);
    }
  }

  if (hasDuplicates(selectedOptions)) {
    document.getElementById("errorMessage").textContent =
      "You are not allowed to choose the same destination more than once.";
  } else {
    document.getElementById("errorMessage").textContent = "";
  }
}

function hasDuplicates(array) {
  return new Set(array).size !== array.length;
}