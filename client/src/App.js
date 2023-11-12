import React, { useState, useEffect} from 'react'
import {Button} from 'antd'

  const App = () => {
    const [clicked, setClicked] = useState(false)
    return (
      <div>
  
          {(clicked) ?(
            <div>
                <Results />
                <Button type='primary' onClick={() => {setClicked(false)}}>Go to Home</Button>
              </div>
            ) : (
              <div>
                <div>Enter data</div>
                <Button onClick={()=>{
                  setClicked(true)
                }} type='primary'>Submit</Button>
              </div>
            )
          }
      </div>
    );
  }
  const Results = () => {
    const [data, setData] = useState([{}])
    useEffect(() => {
        fetch("/results")
          .then(res=>res.json())
          .then(data => {
          setData(data)
          console.log(data)
        })
    }, [])
    return (
      <div>
        {(typeof data.results === "undefined")? (
            <p>loading</p>
          ): (
            data.results.map((result, i)=>(
              <p key={i}>{result}</p>
            ))
          )
        }
      </div>
    )
  }
  export default App