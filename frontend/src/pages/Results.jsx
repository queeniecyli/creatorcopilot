export default function Results({ results, onBack }) {
  return (
    <div className="min-h-screen bg-gradient-to-br from-brand-50 to-blue-50 py-12 px-4">
      <div className="max-w-4xl mx-auto">
        <button
          onClick={onBack}
          className="mb-6 flex items-center text-brand-600 hover:text-brand-700 font-semibold"
        >
          <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 19l-7-7m0 0l7-7m-7 7h18" />
          </svg>
          Back to Generator
        </button>

        <div className="bg-white rounded-2xl shadow-xl p-8 space-y-8">
          <div className="text-center border-b pb-6">
            <h1 className="text-3xl font-bold text-gray-900 mb-2">
              {results.campaign_name || 'Your Campaign Strategy'}
            </h1>
            <p className="text-gray-600">AI-Generated Content Strategy</p>
          </div>

          {results.content_angle && (
            <Section title="Content Angle">
              <p className="text-gray-700 leading-relaxed">{results.content_angle}</p>
            </Section>
          )}

          {results.hook && (
            <Section title="Video Hook" emoji="🎣">
              <div className="bg-brand-50 p-4 rounded-lg border-l-4 border-brand-500">
                <p className="text-gray-800 font-medium">{results.hook}</p>
              </div>
            </Section>
          )}

          {results.script && (
            <Section title="Script" emoji="📝">
              <div className="bg-gray-50 p-6 rounded-lg">
                <p className="text-gray-700 leading-relaxed whitespace-pre-wrap">{results.script}</p>
              </div>
            </Section>
          )}

          {results.shot_list && results.shot_list.length > 0 && (
            <Section title="Shot List" emoji="🎬">
              <ol className="space-y-3">
                {results.shot_list.map((shot, index) => (
                  <li key={index} className="flex items-start">
                    <span className="flex-shrink-0 w-8 h-8 bg-brand-500 text-white rounded-full flex items-center justify-center font-semibold mr-3">
                      {index + 1}
                    </span>
                    <span className="text-gray-700 pt-1">{shot}</span>
                  </li>
                ))}
              </ol>
            </Section>
          )}

          {results.caption && (
            <Section title="Caption" emoji="💬">
              <div className="bg-gray-50 p-6 rounded-lg">
                <p className="text-gray-700 leading-relaxed">{results.caption}</p>
              </div>
            </Section>
          )}

          {results.hashtags && results.hashtags.length > 0 && (
            <Section title="Hashtags" emoji="#️⃣">
              <div className="flex flex-wrap gap-2">
                {results.hashtags.map((tag, index) => (
                  <span
                    key={index}
                    className="bg-brand-100 text-brand-700 px-3 py-1 rounded-full text-sm font-medium"
                  >
                    {tag.startsWith('#') ? tag : `#${tag}`}
                  </span>
                ))}
              </div>
            </Section>
          )}

          {results.cta && (
            <Section title="Call to Action" emoji="📣">
              <div className="bg-brand-50 p-4 rounded-lg border-l-4 border-brand-500">
                <p className="text-gray-800 font-medium">{results.cta}</p>
              </div>
            </Section>
          )}

          {results.recommendations && results.recommendations.length > 0 && (
            <Section title="Optimization Recommendations" emoji="💡">
              <ul className="space-y-3">
                {results.recommendations.map((rec, index) => (
                  <li key={index} className="flex items-start">
                    <svg className="w-6 h-6 text-brand-500 mr-3 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                    </svg>
                    <span className="text-gray-700">{rec}</span>
                  </li>
                ))}
              </ul>
            </Section>
          )}

          <div className="pt-6 border-t">
            <button
              onClick={onBack}
              className="w-full bg-brand-600 hover:bg-brand-700 text-white font-bold py-3 px-6 rounded-lg transition-colors duration-200"
            >
              Create Another Campaign
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

function Section({ title, emoji, children }) {
  return (
    <div>
      <h2 className="text-xl font-bold text-gray-900 mb-4">
        {emoji && <span className="mr-2">{emoji}</span>}
        {title}
      </h2>
      {children}
    </div>
  );
}
