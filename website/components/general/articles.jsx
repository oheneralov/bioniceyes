import React from 'react'

export default function Articles(props) {
  return (
    <section className="jumbotron text-center">
      <div className="container">
        <h1>{props.menu}</h1>
      </div>
    </section>
  )
}
