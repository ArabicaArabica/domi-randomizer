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

//Monad
  var Maybe = {
    Some : function(arr){
      this.arr = arr;
      this.length = arr.length;
      this.bind = function(f){
        return f(this.arr);
      };
    },
    Nothing : function(){
      this.bind = function(){ return this; };
      this.length = 0;
    },
    return : function(arr){ return new Maybe.Some(arr); }
  };
  function first(arr){
    return arr.length === 0 ? new Maybe.Nothing() : new Maybe.Some(arr);
  }
  function reduce(M, f){
    return M.bind(function(arr){ return new Maybe.Some(arr.reduce(f)); });
  }
  function splice(M, a, b){
    return M.bind(function(arr){ return new Maybe.Some(arr.splice(a, b)); });
  }
  function prepare(M){
    if(M.length != 0){
      $("#result").show();
      $("#result > tbody > *").remove();
    }
    return M;
  }

  $("button").click(function(event){
    var candidates = GLOBAL_EXTENDS.filter(function(elem, ind, arr){
      return $("#ex" + ind).prop("checked")
    }).map(function(candidate, i, arr){
      return cards.filter(function(card){
        return card.extend === candidate;
      });
    });
    var cand = prepare(
      reduce(
        first(candidates)
      , function(p, c){ return p.concat(c); }
      )
    );
    _.range(10).map(function(i){
      return splice(
        cand
      , Math.floor(Math.random() * cand.bind(function(arr){ return arr.length; }))
      , 1
      ).bind(function(arr){ return arr[0]; });
    }).forEach(function(elem){
      $("#result > tbody").append($("<tr>")
        .append($("<td>").text(elem.name))
        .append($("<td>").text(elem.extend))
        .append($("<td>").text(elem.cost))
        .append($("<td>").text(elem.potion))
      );
    });
  });
})();
