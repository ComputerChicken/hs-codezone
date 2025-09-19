import { initializeApp } from 'https://www.gstatic.com/firebasejs/12.2.1/firebase-app.js'
import { doc, getDoc, getFirestore } from 'https://www.gstatic.com/firebasejs/12.2.1/firebase-firestore.js'
import 'https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js'

const firebaseConfig = {
  apiKey: "AIzaSyD7USXryTnEIHRxISXxCOQdyD4q7puHuvw",
  authDomain: "codezonehs.firebaseapp.com",
  projectId: "codezonehs",
  storageBucket: "codezonehs.firebasestorage.app",
  messagingSenderId: "564878006133",
  appId: "1:564878006133:web:3acb0b826b57a03943e53c",
  measurementId: "G-B6CZYS7LRS"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app)

const docRef = doc(db, "problems", "problems");
const docSnap = await getDoc(docRef);
const docData = docSnap.data();

async function runPython(pyfile, input) {
  let pyodide = await loadPyodide();
  input = input.replace("^","")

  var msgs = ""
  pyodide.setStdout({
    batched: (msg) => {
      msgs += msg + "\n";
    },
  });

  pyodide.setStdin({
    stdin: () => {
      let userInput = input.split("|||")
      let inputTotal = "";
      userInput.forEach((inp) => {
        inputTotal += inp + "\n"
      })
      console.log(inputTotal)
      return inputTotal
    }
  });


  pyodide.runPython(pyfile);

  return msgs;
}

async function check(problemName, pyfile) {
    const problem = docData[problemName]
    var rTrue = true
    for (const key of Object.keys(problem)) {
        if(key != "NAME" && key != "DIFF" && key != "DESC") {
            const codeResult = await runPython(pyfile,key)
            console.log(codeResult)
            console.log(problem[key])
            if(codeResult == problem[key]) {} else {
                rTrue = false;
            }
        }
    }
    return rTrue;
}

export {check, runPython};