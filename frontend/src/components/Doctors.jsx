import React from 'react'
import { Avatar, Collapse, Grid, Link, Text } from '@nextui-org/react';


function Doctors() {
  <div>
  <title>Doctors</title>
  </div>
  return (
<Grid.Container gap={40}>
  <Grid>
    <Collapse.Group shadow>
      <Collapse title={<Text h4>Dr Joe Bijoy MDS</Text>} subtitle="Orthodontist" contentLeft={
        <Avatar size="lg" src="/avatars/avatar-6.png" color="secondary" bordered squared />
       }>
        <Text>
        An Orthodontist with more than 20yrs of experience is leading the team of our experts. He has about 10yrs of experience working with Ministry of Health, Kuwait as an Orthodontist.
        He is well experienced in Pre adjusted edge-wise, as well as Growth modulation treatment modalities.
        Also handles the cases with Skeletal deformities of the face.
        </Text>
      </Collapse>
      <Collapse title={<Text h4>Dr A Devadathan MDS</Text>} subtitle="Endodontist" contentLeft={
        <Avatar size="lg" src="/avatars/avatar-3.png" color="success" bordered squared />
      }>
        <Text>
        He is our Endodontist with 20yrs of experience. 
        Currently he is the Vice Principal of Pushpaghiri College of Dental Sciences, Thiruvalla. An expert in his field, and a renowned Academician. 
        He is also a panel member in the board of examiners of M.G. University.
        </Text>
      </Collapse>
      <Collapse title={<Text h4>Dr Arun Babu MDS</Text>} subtitle="Oral & Maxillo-Facial Surgeon"contentLeft={
        <Avatar size="lg" src="/avatars/avatar-5.png" color="error" bordered squared />
      }>
        <Text>
        Our Oral & Maxillo-Facial Surgeon, an expert in trauma and Orthognathic Surgeries.
        He is also an expert in Implantology and has more than 18yrs of experience. 
        He is the Consultant Oral and Maxillo-Facial surgeon to Mar Gregarious Hospital and KVM Hospital.
        </Text>
      </Collapse>
      <Collapse title={<Text h4>Dr Binoy Mathew MDS</Text>} subtitle="Prosthodontist"contentLeft={
        <Avatar size="lg" src="/avatars/avatar-4.png" color="primary" bordered squared />
      }>
        <Text>
        A well experienced Prosthodontist handles our Prosthodontic Dept and has about 13yrs of experience. 
        He deals with Crown & Bridges, Dentures, Cast prosthesis as well as Eye prosthesis. 
        He is also well trained in Implantology. 
        Currently he is Asso.Prof in the Dept of Prosthodontics, Pushpaghiri College of Dental Sciences, Thiruvalla.
        </Text>
      </Collapse>
      <Collapse title={<Text h4>Dr Nebu George MDS</Text>} subtitle="Periodontist"contentLeft={
        <Avatar size="lg" src="/avatars/avatar-4.png" color='warning' bordered squared />
      }>
        <Text>
        A Periodontist with more than 11yrs of practice deals with all issues related to gums and supporting tissues.
        Also deals with Bone Grafting, Flap treatments etc. 
        Also an Implantologist, he is Assi. Prof. Dept of Periodontics, Puspaghiri College of Dental Sciences, Thiruvalla.
        </Text>
      </Collapse>
    </Collapse.Group>
  </Grid>    
</Grid.Container>

  )
}

export default Doctors