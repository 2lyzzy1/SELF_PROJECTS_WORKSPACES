
/* Defining Var. & Const. Data &/|| Objects */
/* Objects */
const labels = document.querySelectorAll('label');
const spanAnimat = document.getElementsByClassName('span_');
/* Data Fields */
const lastNameField = document.getElementById("lastName");
const firstNameField = document.getElementById("firstName");
const emailField = document.getElementById("eMail");
const passwordField = document.getElementById("passWord");
/* Data */
var userFirstName_="", userLastName_="", userEmailAddress_="", userPassWord_="", userNewPassWord_="", userModifiedPassWord_="";
const name_ = "rootUser";
const email_ = 'rootuser@email.com' || 'rootuser@gmail.com';
const passWord_ = 1111;

/* --------------------------------------------------------------- */
/* Stylizing Objects */
labels?.forEach(label => {
  label.addEventListener('click',
    () => {
      label.style.position = 'absolute';
      label.style.width = '0';
      label.style.backgroundColor = '#000000';
    }
  )
});


/* --------------------------------------------------------------- */
/* Collecting::Data||Informations */

lastNameField?.addEventListener("change", () => {
  userLastName_ = lastNameField.value;
})
firstNameField?.addEventListener("change", () => {
  userFirstName_ = firstNameField.value;
})
emailField?.addEventListener("change", () => {
  userEmailAddress_ = emailField.value;
})
passwordField?.addEventListener("change", () => {
  userPassWord_ = passwordField.value;
})

const userData_ = {
  userFirstName: userFirstName_,
  userLastName: userLastName_,
  userEmailAddress: userEmailAddress_,
  userPassWord: userPassWord_,
  userNewPassWord: () => { const tempNewPass ="&ggqf²fff_w________çw878"; return tempNewPass; },
  userModifiedPassWord: () => { const tempModPass = "3279836V  v v vSvgvs"; return tempModPass; },
};

function HandleSubmit () {
  console.log(userData_, userData_.userLastName);
  setTimeout(() => {
    window.location.assign("http://gemini.google.com/");
  }, 10000);
}

/* --------------------------------------------------------------- */
/* Manipulating::Data */

const getUserId = () => {};
/* onConn */
const verifyUserId = () => {
  //
};
/* --------------------------------------------------------------- */

// HandleSubmit();


/* --------------------------------------------------------------- */
/* export */

// export default HandleSubmit;

