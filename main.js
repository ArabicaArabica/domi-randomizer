(function(){
  "use strict";
  function Card(data){
    var self = this;
    self.name = data[0];
    self.extend = data[1];
    self.cost = data[2];
    self.potion = data[3];

    self.isBane = function(){
      return self.cost === 2 || self.cost === 3;
    };
  }
  var cards = GLOBAL_CARDS.map(function(card){
    return new Card(card);
  });
  $("#result").hide();
  GLOBAL_EXTENDS.forEach(function(elem, i){
    $("#specify_set").append($("<input>")
      .attr("type", "checkbox")
      .attr("id", "ex" + i)
    ).append($("<label>")
      .text(elem)
    );
  });

  $("button").click(function(event){
    try{
      var candidates = GLOBAL_EXTENDS.filter(function(elem, ind, arr){
        return $("#ex" + ind).prop("checked")
      }).map(function(candidate, i, arr){
        return cards.filter(function(card){
          return card.extend === candidate;
        });
      }).reduce(function(p, c){
        return p.concat(c);
      });
      var results = _.range(10).map(function(i){
        return candidates.splice(
          Math.floor(Math.random() * candidates.length), 1
        )[0];
      });
    }catch(e){
      return ;
    }
    $("#result").show();
    $("#result > tbody > *").remove();
    results.forEach(function(elem){
      $("#result > tbody").append($("<tr>")
        .append($("<td>").text(elem.name))
        .append($("<td>").text(elem.extend))
        .append($("<td>").text(elem.cost))
        .append($("<td>").text(elem.potion))
      );
    });
  });
})();
