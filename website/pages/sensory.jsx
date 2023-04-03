import Link from 'next/link'
import SimpleLayout from '../components/layout/simple'
import ArticlesJumbo from '../components/general/articles'

export default function Sensory(initialData) {
  return (
    <SimpleLayout preContainer={<ArticlesJumbo menu="Sensory substitution"  />}>
      <div className="row">
        <div className="col-md-4">
          <div className="card mb-4 shadow-sm">
            <Link href={`/#`}><a>
              <svg className="bd-placeholder-img card-img-top" width="100%" height="225" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Thumbnail" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#55595c"/><text x="50%" y="50%" fill="#eceeef" dy=".3em">Thumbnail</text></svg>
            </a></Link>
            <div className="card-body">
              <h3>Article 1</h3>
              <p className="card-text">{initialData.data.content.Sensory}</p>
            </div>
          </div>
        </div>
      </div>
    </SimpleLayout>
  )
}

// This gets called on every request
export async function getServerSideProps(context) {
  const host = context.req.headers.host
  // Fetch data from external API
  const res = await fetch(`http://${host}/data.json`)
  const data = await res.json()

  // Pass data to the page via props
  return { props: { data } }
}
