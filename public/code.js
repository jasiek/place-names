(function() {
  var search_term = document.getElementById("s");
  var submit = document.getElementById("submit");
  var results = document.getElementById("results");
  submit.addEventListener("click", function() {
    fetch("/search?s=" + search_term.value, { method: "get" })
      .then(response => response.json())
      .then(function(j) {
        while (results.hasChildNodes()) {
          results.removeChild(results.firstChild);
        }
        j.forEach(function(e) {
          var tr = document.createElement("tr");
          var td = document.createElement("td");
          var text = document.createTextNode(e);
          td.appendChild(text);
          tr.appendChild(td);
          results.appendChild(tr);
        });
      })
  });
})();
