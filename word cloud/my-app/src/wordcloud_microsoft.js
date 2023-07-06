import React, { useEffect, useState } from 'react';
import WordCloud from 'react-wordcloud';
import data from 'C:\Users\karth\AppData\Local\Programs\Python\Python311\Coforge\word cloud\my-app\src\extracted_data_gcp_microsoft.json';

const WordCloudComponent = () => {
  const [verbs, setVerbs] = useState([]);

  useEffect(() => {
    // Extract verbs from the JSON data
    const extractedVerbs = data.map(item => item.verb);
    setVerbs(extractedVerbs);
  }, []);

  return (
    <div>
      <h2>Word Cloud</h2>
      <WordCloud words={verbs} />
    </div>
  );
};

export default WordCloudComponent;
