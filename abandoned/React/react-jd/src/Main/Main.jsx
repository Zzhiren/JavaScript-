import React from 'react'
import TopPromotion from '../components/TopPromotion/TopPromotion'
import Navigation from '../components/Navigation/Navigation'
export default class Main extends React.Component{
  render() {
    return (
      <div>
        <TopPromotion></TopPromotion>
        <Navigation></Navigation>
      </div>
    )
  }
}