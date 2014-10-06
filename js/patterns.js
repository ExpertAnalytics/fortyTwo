
/*
 * Some patterns that have proven to be useful in other places, written in a 
 * standalone way.
 */

// 
// Create a closure where we can store data
//
// Usage: 
//
// Application.set_data(key, 'some value');
// field = Application.get_data(key);
//
// Note; if an object (array, dictionary, o.a) is added with set_data, 
// we will get a reference back with get_data - this is often handy. I.e. we
// can just update the reference, and the data in Application is automatically
// updated - no need to set it again.
var Application = function() {
   var data = [];

   return {
      set_data: function (field, val) { data[field] = val; },
      get_data: function (field) { return data[field]; },
   };
}();


// Assume that you need to run severeal functions async, and when the last one 
// finish, you want to run a callback/continuation. We assume that all the 
// functions take a callback as an argument
// We assume that all functions run the callback regardless of status (i.e.
// proper error-handling)
//

var run_functions_callback_on_last = function run_functions_callback_on_last(funcs, continuation) {

   var continuation_wrap = null;;

   if (typeof(continuation) === "function") {
      var cont_id = "cont_" + randint(1, 10000000);
      // store one real continuation, and then length(functions) - 1 'fake'
      var continuations = [];
      continuations.push(continuation);
      $.each(functions, function(idx, item) { continuations.push(''); });
      // we got one to many, pop the last one off again.
      continuations.pop();
      // Store the list in Application
      Application.set_data(cont_id, continuations);

      // create a wrapper that will pop off the continuations, and at the final 
      // pop run the true continuation

      continuation_wrap = function() {
         var cont = Application.get_data(cont_id).pop();
         if (typeof(cont) === "function") {
            cont();
         }
      }
   }

   $.each(functions, function(idx, fu) {
      fu(continuation_wrap);
   });
}


var randint = function randint(min, max) { 
   return Math.floor(Math.random() * (max - min) + min);
}
