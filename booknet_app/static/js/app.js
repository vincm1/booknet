function refreshDiv(footernewsletter) {
    $("#" + footernewsletter).load(document.URL +  " #" + divId);
  }