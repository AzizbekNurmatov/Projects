import React, { useEffect, useState } from 'react'

 const useFetch = (url) => {
    const[data,setData]=useState();
    useEffect(()=>{
        fetch(url).then((res)=>res.json())
        .then((data)=>setData(data))
    },[])
  return [data]
}

export default useFetch
// Example of custom hook to fetch data from an api and display it in a component