import Head from 'next/head'
import SimpleLayout from '../components/layout/simple'

export default function Home(initialData) {
  return (
    <SimpleLayout>
      <section className="jumbotron text-center">
        <div className="container">
          <p className="lead text-muted">
            Home
          </p>
        </div>
      </section>

      <div className="row">
        <h1>Hey People</h1>
      </div>
      <div className="row">
        <p>
          Bootstrap is awesome
        </p>
      </div>
    </SimpleLayout>
  )
}
