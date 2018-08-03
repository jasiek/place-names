(function() {
  var search_term = document.getElementById("s");
  var submit = document.getElementById("submit");
  var results = document.getElementById("results");
  var certain = document.getElementById("certain");
  submit.addEventListener("click", function() {
    while (results.hasChildNodes()) {
      results.removeChild(results.firstChild);
    }
    var url = "/search?s=" + search_term.value;
    if (certain.checked) {
      url += "&certain=yes";
    }
    fetch(url, { method: "get" })
      .then(function(r) { return r.json() })
      .then(function(j) {
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
