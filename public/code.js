(function() {
  var search_term = document.getElementById("s");
  var submit = document.getElementById("submit");
  var results = document.getElementById("results");
  var certain = document.getElementById("certain");
  submit.addEventListener("click", function() {
    var url = "/search?s=" + search_term.value;
    if (certain.value) {
      url += "&certain=yes";
    }
    fetch(url, { method: "get" })
      .then(function(r) { return r.json() })
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
