// script.js
// |---------------------------->

// REDIRECTION FUNCTION
// ----------------------------------------------------------------------
const redirect = (link_, stime = 2000, api_ = "window") => {
  setTimeout(() => {
    switch (api_) {
      case "window":
        window.location.assign(link_); // '../../*.html' | '../../*.*'
        break
      case "aHref":
        window.location.assign(link_); // '../../*.html' | '../../*.*'
        break
    }
  }, stime);
}


// TIMER HANDLER FUNCTION
// ----------------------------------------------------------------------
const timeBoxId = "timeStamp";
const timeDisplayer = document.getElementById(timeBoxId);

// Timer Controller
/*
const timedTasks = [
  () => new Promise(res => 
  () => {
    setTimeout(() => {
      // for (let j=0; j<2; j++) {
        let i = 0;
        let loading_ = `loading .`;
        const loading = setInterval(() => {
          timeDisplayer?.innerHTML = loading_;
          loading_ = loading_ +'.';
          if ((i+1)%3===0) { loading_=`loading .`; }
          if (i===11) { clearInterval(loading); }
          i++;
        }, 500);
      // } i3 - p4
    }, 1000)
    res();
  }
  ),
  //
  () => new Promise(res => 
  () => {
    setInterval(() => {
      const localDateTimeZone = new Date();
      timeDisplayer.innerHTML =
       `${localDateTimeZone}`;
      // res();
    }, 1000)
    res();
  }
  ),
];

async function runAsyncTimer() {
  for (const asyncTask of timedTasks) {
    await asyncTask(); // chaque tâche attend la précédente
  }
}
// runAsyncTimer();  // new Learn();  | in timer
*/

// -------------------------------------------------
const timer = /* async */ (o='timeStamp') => {
  // const timeDisplayer = document.getElementById(o);
  // o = this;
  const localTime = {};
  const localDateTimeZone = new Date();
  const localDate = localDateTimeZone.getDay() +' '+ localDateTimeZone.getDate();
  const localYears = localDateTimeZone.getFullYear();
  const localHours = localDateTimeZone.getHours();
  // o.innerHTML = localDateTimeZone;

  if (window.GeolocationCoordinates) {
		timeDisplayer.innerHTML = window.Geolocation;
	}
	///*
	setTimeout(() => {
		// for (let j=0; j<2; j++) {
			let i = 0;
			let loading_ = `loading .`;
			const loading = setInterval(() => {
				timeDisplayer.innerHTML = loading_;
				loading_ = loading_ +'.';
				if ((i+1)%3===0) { loading_=`loading .`; }
				if (i===11) { clearInterval(loading); }
				i++;
			}, 500);
		// } i3 - p4
	}, 1000);//*/
	//
  /* await *////*
  setInterval(() => {
		const localDateTimeZone = new Date();
    timeDisplayer.innerHTML =
     `${localDateTimeZone}`;
  }, 1000);//*/

  // runAsyncTimer();  // new Learn();

  // return localDateTimeZone;
}

timer();


// 
// ----------------------------------------------------------------------


// 

