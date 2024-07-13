<!DOCTYPE html>
<html>
<body>

<h1>VAHNINETRA: AI in Workplace Health & Safety</h1>

<p>A <strong>Fire Alarm System</strong> warns people when smoke, fire, carbon monoxide, or other fire-related or general notification emergencies are detected. These alarms may be activated automatically from smoke detectors and heat detectors or may also be activated via manual fire alarm activation devices such as manual call points or pull stations. Alarms can be either motorized bells or wall mountable sounders or horns.</p>

<h2>Problem Statement</h2>
<p>The primary issue is the susceptibility to delayed alarms, which can lead to complacency and diminished trust in the alarm system, potentially resulting in inappropriate responses.</p>

<h2>Proposed Solution: VAHNINETRA</h2>

<h3>Fire & Smoke Alarm System</h3>
<ul>
  <li>Fire in commercial spaces, especially manufacturing plants, are serious accidents that can cause unprecedented loss of goods, company assets and human life.</li>
  <li>Smart fire & smoke detectors are built using artificial intelligence and machine learning models to detect smoke emissions in an industrial setting and send real-time alerts to help control fire and its hazardous effects.</li>
  <li>Implementing smart fire & smoke detectors for industries is an effective solution for improving fire safety. With advanced features such as remote monitoring, accuracy and reliability compared to previous-generation detectors, this technology is a necessity for modern industrial environments.</li>
</ul>

<h3>Workflow</h3>
<ol>
  <li>Dataset</li>
  <li>Image Preprocessing</li>
  <li>Train Test Split</li>
  <li>Model Making</li>
  <li>Evaluation</li>
</ol>

<h3>Dataset</h3>
<p>Data can be taken from sensors which can directly be uploaded on CLOUD, and can be instantly interfaced with our model.</p>
<p>Link to Dataset: <a href="https://github.com/dvvansia1805/Vahninetra-AI-Workspace-Health-Safety/blob/main/smoke_detection_iot.csv">https://github.com/dvvansia1805/Vahninetra-AI-Workspace-Health-Safety/blob/main/smoke_detection_iot.csv</a></p>

<h3>Parameters in the Dataset</h3>
<ul>
  <li><strong>UTC:</strong> Time when the experiment was performed.</li>
  <li><strong>Temperature[C]:</strong> Temperature of surroundings, measured in Celsius.</li>
  <li><strong>Humidity[%]:</strong> Air humidity during the experiment.</li>
  <li><strong>TVOC[ppb]:</strong> Total Volatile Organic Compounds, measured in ppb (parts per billion).</li>
  <li><strong>eCO2[ppm]:</strong> CO2 equivalent concentration, measured in ppm (parts per million).</li>
  <li><strong>Raw H2:</strong> The amount of Raw Hydrogen [Raw Molecular Hydrogen; not compensated (Bias, Temperature, etc.)] present in surroundings.</li>
  <li><strong>Raw Ethanol:</strong> The amount of Raw Ethanol present in surroundings.</li>
  <li><strong>Pressure[hPa]:</strong> Air pressure, Measured in hPa.</li>
  <li><strong>PM1.0:</strong> Particulate matter of diameter less than 1.0 micrometer.</li>
  <li><strong>PM2.5:</strong> Particulate matter of diameter less than 2.5 micrometers.</li>
  <li><strong>NC0.5:</strong> Concentration of particulate matter of diameter less than 0.5 micrometer.</li>
  <li><strong>NC1.0:</strong> Concentration of particulate matter of diameter less than 1.0 micrometer.</li>
  <li><strong>NC2.5:</strong> Concentration of particulate matter of diameter less than 2.5 micrometers.</li>
  <li><strong>CNT:</strong> Sample Count.</li>
  <li><strong>Fire Alarm:</strong> <strong>1</strong> means <strong>Positive</strong> and <strong>0</strong> means <strong>Not Positive</strong>. Fire Alarm (Reality) If the fire was present then the value is 1 else it is 0.</li>
</ul>

<h3>Classifier Models</h3>
<ol>
  <li>Logistic Regression</li>
  <li>Support Vector Machines</li>
  <li>Bernoulli Naïve Bayes</li>
  <li>Gaussian Naïve Bayes</li>
  <li>K- Nearest Neighbour</li>
  <li>Random Forest</li>
</ol>

<h3>Why VahniNetra?</h3>
<ul>
  <li>Our Model is more accurate and reliable than traditional fire & smoke detectors, which often fail to detect smoke on time or are triggered by false alarms.</li>
  <li>The advent of AI-powered wireless technology in smoke detectors has encouraged small-medium businesses to invest in fire safety systems.</li>
  <li>Our model can provide remote monitoring and remote alerting to specified field operators.</li>
  <li>Traditional fire and Smoke detectors lack in detection of small fires and fumes (typically caused by raw hydrogen).</li>
  <li>Compared to traditional fire and smoke detectors, our model can provide live data about atmospheric conditions.</li>
  <li>In industries, the traditional detectors are installed at high ceilings causing delay in detection of fire and smoke.</li>
</ul>

<h3>Applications</h3>
<ul>
  <li>Industries</li>
  <li>Space Craft</li>
  <li>Huge Malls & Multiplexes</li>
  <li>Textiles & Factories</li>
</ul>

</body>
</html>
