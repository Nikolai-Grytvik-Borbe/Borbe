import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <h1>Borbe.no</h1>
//       </header>
//       <main>
//         <h3 className="App-text">A portfolio/blog project by Fredrik and Nikolai Borbe</h3>
//       </main>
//       <footer className="footer">
//         <small>© 2022 Fredrik Borbe, Nikolai Borbe, </small>
//       </footer>
//     </div>
//   );
// }

function App() {
  return(
    <>
      <div class="split left">
        <div class="centered">
          <h2>Nikolai</h2>
          <p>Some text.</p>
        </div>
      </div>

      <div class="split right">
        <div class="centered">
          <h2>Fredrik</h2>
          <p>Some text here too.</p>
        </div>
      </div>
    </>
  )
}

export default App;
