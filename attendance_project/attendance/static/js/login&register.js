function myFunction() {
  var x = document.getElementById("mypassword");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}
// // this is validation of register page
// $(document).on('click', '#savebtn', function (event) {
//   event.preventdefault()
//   // console.log('jhbzhjcbjc')
//   let uname = $('#username').val()
//   // console.log(uname)
//   let email = $('#email').val()
//   // console.log(email)
//   let pass1 = $('#password').val()
//   // console.log(pass1)
//   let pass2 = $('#c_password').val()
//   // let csr = $('input[name= csrfmiddlewaretoken]').val();
//   // console.log(pass2)
//   if (uname == '') {
//     // let nm = $('span').val('plzz enter the name')\
//     $('#uname').append('please enter the name ')
//   }
//   else if (email == '') {
//     $('#em').append('email is not validated')

//   }
//   else if (pass1 == '') {
//     $('#pass_alert1').append('plzz enter the password')

//   }
//   else if (pass2 == '') {
//     $('#pass_alert2').append('plzz enter the password')

//   }
//   else {
//     console.log(uname)
//     console.log(email)
//     console.log(pass1)
//     console.log(pass2)
//     // my_data = { name: uname, email: email };
//     // $.ajax({
//     //   url: "/save_register/",
//     //   method: "POST",
//     //   data: mydata,
//     //   success: function (data) {
//     //     console.log(mydata)

//     //   }
//     // })
//   }



// })

// // this is login page validation
// // $('#login_id').on('click', function(e){
// //   e.preventdefault();
// //   let Uname = $('#uname').val();
// //   console.log(Uname)
// //   let pass = $('#mypassword').val()
// //   console.log(pass)
// // })